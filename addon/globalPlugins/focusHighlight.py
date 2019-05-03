# focus highlight
# 2019-05-03
# Takuya Nishimoto

import sys
import threading
import time
from ctypes import (WINFUNCTYPE, FormatError, GetLastError, Structure,
                    WinError, byref, c_char, c_char_p, c_float, c_int, c_long,
                    c_uint, c_uint32, c_ulong, c_void_p, pointer, windll)
from ctypes.wintypes import BOOL, COLORREF
try:
    from ctypes import POINTER
except:
    from ctypes.wintypes import POINTER

import api
import controlTypes
import globalPluginHandler
import gui
import oleacc
import speech
import tones
import ui
import virtualBuffers
import winUser
import wx
from logHandler import log
from NVDAObjects import NVDAObject
from win32con import (CS_HREDRAW, CS_VREDRAW, CW_USEDEFAULT, GWL_EXSTYLE,
                      GWL_STYLE, HS_BDIAGONAL, HS_DIAGCROSS, HWND_DESKTOP,
                      HWND_TOPMOST, IDC_ARROW, LWA_ALPHA, LWA_COLORKEY, NULL,
                      SW_HIDE, SW_SHOWNA, SWP_NOACTIVATE, WM_DESTROY,
                      WM_ERASEBKGND, WM_PAINT, WM_SHOWWINDOW, WM_TIMER,
                      WS_CAPTION, WS_DISABLED, WS_EX_APPWINDOW, WS_EX_LAYERED,
                      WS_EX_TOOLWINDOW, WS_EX_TRANSPARENT, WS_POPUP,
                      WS_VISIBLE)
try:
	from windowUtils import physicalToLogicalPoint
except:
	physicalToLogicalPoint = None

try:
	from core import callLater
except:
	callLater = wx.CallLater

gdiplus = windll.gdiplus

WNDPROC = WINFUNCTYPE(c_long, c_int, c_uint, c_int, c_int)


class WNDCLASS(Structure):
	_fields_ = [('style', c_uint),
				('lpfnWndProc', WNDPROC),
				('cbClsExtra', c_int),
				('cbWndExtra', c_int),
				('hInstance', c_int),
				('hIcon', c_int),
				('hCursor', c_int),
				('hbrBackground', c_int),
				('lpszMenuName', c_char_p),
				('lpszClassName', c_char_p)]


class RECT(Structure):
	_fields_ = [('left', c_long),
				('top', c_long),
				('right', c_long),
				('bottom', c_long)]


class PAINTSTRUCT(Structure):
	_fields_ = [('hdc', c_int),
				('fErase', c_int),
				('rcPaint', RECT),
				('fRestore', c_int),
				('fIncUpdate', c_int),
				('rgbReserved', c_char * 32)]


class POINT(Structure):
	_fields_ = [('x', c_long),
				('y', c_long)]


class MSG(Structure):
	_fields_ = [('hwnd', c_int),
				('message', c_uint),
				('wParam', c_int),
				('lParam', c_int),
				('time', c_int),
				('pt', POINT)]


class GdiplusStartupInput(Structure):
	_fields_ = [
		('GdiplusVersion', c_uint32),
		('DebugEventCallback', c_void_p),
		('SuppressBackgroundThread', BOOL),
		('SuppressExternalCodecs', BOOL)
	]


class GdiplusStartupOutput(Structure):
	_fields = [
		('NotificationHookProc', c_void_p),
		('NotificationUnhookProc', c_void_p)
	]


c_void_p_p = POINTER(c_void_p)

# GpStatus WINGDIPAPI GdipCreateFromHDC(HDC hdc, GpGraphics **graphics);
gdiplus.GdipCreateFromHDC.argtypes = [c_int, c_void_p_p]
gdiplus.GdipCreateFromHDC.restype = c_int

# GpStatus WINGDIPAPI GdipCreatePen1(
#  ARGB color, (DWORD = c_int)
#  REAL width, (float = c_float)
#  GpUnit unit, (enum = c_int)
#	 0: world (non-physical) coordinates
#	 2: Each unit is one device pixel
#  GpPen **pen	(c_void_p_p)
# );
gdiplus.GdipCreatePen1.argtypes = [c_int, c_float, c_int, c_void_p_p]
gdiplus.GdipCreatePen1.restype = c_int

# GpStatus WINGDIPAPI GdipSetPenDashStyle(GpPen*,GpDashStyle);
gdiplus.GdipSetPenDashStyle.argtypes = [c_void_p, c_int]
gdiplus.GdipSetPenDashStyle.restype = c_int

# GpStatus WINGDIPAPI GdipDrawLine(GpGraphics *graphics, GpPen *pen, REAL x1, REAL y1, REAL x2, REAL y2);
gdiplus.GdipDrawLine.argtypes = [c_void_p, c_void_p, c_float, c_float, c_float, c_float]
gdiplus.GdipDrawLine.restype = c_int

# GpStatus WINGDIPAPI GdipDrawRectangle(GpGraphics *graphics, GpPen *pen, REAL x, REAL y, REAL w, REAL h);
gdiplus.GdipDrawRectangle.argtypes = [c_void_p, c_void_p, c_float, c_float, c_float, c_float]
gdiplus.GdipDrawRectangle.restype = c_int

# GpStatus WINGDIPAPI GdipDeletePen(GpPen *pen);
gdiplus.GdipDeletePen.argtypes = [c_void_p]
gdiplus.GdipDeletePen.restype = c_int

# GpStatus WINGDIPAPI GdipDeleteGraphics(GpGraphics *graphics);
gdiplus.GdipDeleteGraphics.argtypes = [c_void_p]
gdiplus.GdipDeleteGraphics.restype = c_int


def ErrorIfZero(handle):
	if handle == 0:
		raise WinError()
	else:
		return handle


ERROR_CLASS_HAS_WINDOWS = 1412


def RGB(r,g,b):
	return r | (g<<8) | (b<<16)


def makeARGB(a,r,g,b):
	return (a<<24) | (r<<16) | (g<<8) | b


CreateWindowEx = windll.user32.CreateWindowExA
CreateWindowEx.argtypes = [c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]
CreateWindowEx.restype = ErrorIfZero

# Transparent color key
TRANS_RGB = RGB(0, 0, 0)
transColor = COLORREF()
transColor.value = TRANS_RGB
transBrush = windll.gdi32.CreateSolidBrush(transColor)

# focus (passthrough)
ptARGB = makeARGB(255, 0x22, 0x22, 0xff)
ptDashStyle = 2
ptThickness = 12

# focus
fcARGB = makeARGB(255, 0xff, 0x00, 0x00)
fcDashStyle = 0
fcThickness = 6

# navigator
navARGB = makeARGB(255, 0x00, 0xff, 0x00)
navDashStyle = 3
navThickness = 4

PADDING_THIN = 10
PADDING_THICK = 5
WINDOW_ALPHA = 192

ID_TIMER = 100
UPDATE_PERIOD = 300

focusRect = RECT()
focusHwnd = 0

navigatorRect = RECT()
navigatorHwnd = 0

wndclass = None
preparing = True
terminating = False
passThroughMode = True
currentAppSleepMode = False


def rectEquals(r1, r2):
	return (r1.top == r2.top and r1.bottom == r2.bottom and r1.left == r2.left and r1.right == r2.right)


def location2rect(location):
	rect = RECT()
	if location and len(location) >= 4:
		rect.left = location[0]
		rect.top = location[1]
		rect.right = rect.left + location[2]
		rect.bottom = rect.top + location[3]
	return rect


def physicalRectToLogicalLocation(hwnd, rect, margin=15):
	if physicalToLogicalPoint:
		left, top = physicalToLogicalPoint(hwnd, rect.left - margin, rect.top - margin)
		right, bottom = physicalToLogicalPoint(hwnd, rect.right + margin, rect.bottom + margin)
		return left, top, right - left, bottom - top
	return (
		(rect.left - margin),
		(rect.top - margin),
		(rect.right - rect.left + margin * 2),
		(rect.bottom - rect.top + margin * 2)
	)


def moveAndShowWindow(hwnd, rect):
	if not hwnd: return
	left, top, width, height = physicalRectToLogicalLocation(hwnd, rect)
	windll.user32.ShowWindow(c_int(hwnd), SW_HIDE)
	windll.user32.MoveWindow(c_int(hwnd), left, top, width, height, True)
	windll.user32.ShowWindow(c_int(hwnd), SW_SHOWNA)


def locationAvailable(obj):
	return (obj and hasattr(obj, 'location') and obj.location and len(obj.location) >= 4)


def isPassThroughMode():
	focus = api.getFocusObject()
	if hasattr(focus, 'treeInterceptor') and focus.treeInterceptor:
		return bool(focus.treeInterceptor.passThrough)
	return True


def isCurrentAppSleepMode():
	focus = api.getFocusObject()
	if hasattr(focus, 'appModule') and focus.appModule:
		return focus.appModule.sleepMode
	return False


def updateFocusLocation():
	global focusRect
	focus = api.getFocusObject()
	if locationAvailable(focus):
		newRect = location2rect(focus.location)
	else:
		return
	if not rectEquals(newRect, focusRect):
		focusRect = newRect
		moveAndShowWindow(focusHwnd, focusRect)


def updateNavigatorLocation():
	global navigatorRect
	try:
		nav = api.getNavigatorObject()
	except:
		return
	if not isinstance(nav, NVDAObject):
		return
	if locationAvailable(nav):
		newRect = location2rect(nav.location)
	elif locationAvailable(api.getFocusObject()):
		newRect = location2rect(api.getFocusObject().location)
	else:
		return
	if not rectEquals(newRect, navigatorRect):
		navigatorRect = newRect
		moveAndShowWindow(navigatorHwnd, navigatorRect)


def createMarkWindow(name, hwndParent, rect):
	global wndclass
	hwnd = CreateWindowEx(0,
						wndclass.lpszClassName,
						name,
						WS_POPUP|WS_DISABLED,
						CW_USEDEFAULT,
						CW_USEDEFAULT,
						CW_USEDEFAULT,
						CW_USEDEFAULT,
						hwndParent,
						NULL,
						wndclass.hInstance,
						NULL)
	left, top, width, height = physicalRectToLogicalLocation(hwnd, rect)
	windll.user32.SetWindowPos(c_int(hwnd), HWND_TOPMOST, left, top, width, height, SWP_NOACTIVATE)
	exstyle = windll.user32.GetWindowLongA(c_int(hwnd), GWL_EXSTYLE)
	exstyle &= ~WS_EX_APPWINDOW
	exstyle |= WS_EX_TOOLWINDOW | WS_EX_LAYERED | WS_EX_TRANSPARENT
	windll.user32.SetWindowLongA(c_int(hwnd), GWL_EXSTYLE, exstyle)
	windll.user32.SetLayeredWindowAttributes(c_int(hwnd), TRANS_RGB, WINDOW_ALPHA, LWA_ALPHA|LWA_COLORKEY)
	windll.user32.ShowWindow(c_int(hwnd), SW_SHOWNA)
	windll.user32.UpdateWindow(c_int(hwnd))
	return hwnd


def doPaint(hwnd):
	rect = RECT()
	windll.user32.GetClientRect(c_int(hwnd), byref(rect))
	ps = PAINTSTRUCT()
	hdc = windll.user32.BeginPaint(c_int(hwnd), byref(ps))
	#log.debug("BeginPaint hdc {0!r}".format(hdc))
	windll.user32.FillRect(hdc, byref(rect), transBrush)

	argb, dashStyle, thickness, padding = None, None, None, None
	if hwnd == focusHwnd:
		if currentAppSleepMode:
			pass
		elif passThroughMode:
			argb, dashStyle, thickness, padding = ptARGB, ptDashStyle, ptThickness, PADDING_THICK
		else:
			argb, dashStyle, thickness, padding = fcARGB, fcDashStyle, fcThickness, PADDING_THICK
		if rectEquals(focusRect, navigatorRect):
			if not passThroughMode and thickness is not None:
				thickness *= 2
			padding = PADDING_THICK
	else:
		if currentAppSleepMode:
			pass
		elif rectEquals(focusRect, navigatorRect):
			pass
		else:
			argb, dashStyle, thickness, padding = navARGB, navDashStyle, navThickness, PADDING_THIN

	if argb is None:
		windll.user32.EndPaint(c_int(hwnd), byref(ps))
		return

	gpGraphics = c_void_p()

	gpStatus = gdiplus.GdipCreateFromHDC(hdc, byref(gpGraphics))
	#log.debug("GdipCreateFromHDC gpStatus {0!r} gpGraphics {1!r}".format(gpStatus, gpGraphics))

	gpPen = c_void_p()

	gpStatus = gdiplus.GdipCreatePen1(argb, thickness, 2, byref(gpPen))
	#log.debug("GdipCreatePen1 gpStatus {0!r} gpPen {1!r}".format(gpStatus, gpPen))

	gpStatus = gdiplus.GdipSetPenDashStyle(gpPen, dashStyle)
	#log.debug("GdipSetPenDashStyle gpStatus {0!r}".format(gpStatus))

	l = rect.left
	t = rect.top
	r = rect.right
	b = rect.bottom
	gdiplus.GdipDrawRectangle(gpGraphics, gpPen, float(l+padding), float(t+padding), float(r-l-padding*2), float(b-t-padding*2))

	gpStatus = gdiplus.GdipDeletePen(gpPen)
	#log.debug("GdipDeletePen gpStatus {0!r}".format(gpStatus))

	gpStatus = gdiplus.GdipDeleteGraphics(gpGraphics)
	#log.debug("GdipDeleteGraphics gpStatus {0!r}".format(gpStatus))

	windll.user32.EndPaint(c_int(hwnd), byref(ps))


def invalidateRects():
	for hwnd in (focusHwnd, navigatorHwnd):
		if hwnd:
			windll.user32.InvalidateRect(c_int(hwnd), None, True)


def updateLocations():
	global passThroughMode, currentAppSleepMode
	passThroughMode = isPassThroughMode()
	currentAppSleepMode = isCurrentAppSleepMode()
	updateFocusLocation()
	updateNavigatorLocation()
	invalidateRects()


def wndProc(hwnd, message, wParam, lParam):
	if message == WM_PAINT:
		doPaint(hwnd)
		return 0
	elif message == WM_DESTROY:
		windll.user32.PostQuitMessage(0)
		return 0
	elif message == WM_SHOWWINDOW:
		if hwnd == focusHwnd:
			timer = windll.user32.SetTimer(c_int(hwnd), ID_TIMER, UPDATE_PERIOD, None)
		return 0
	elif message == WM_TIMER:
		if not preparing and hwnd == focusHwnd and not terminating:
			updateLocations()
		return 0
	return windll.user32.DefWindowProcA(c_int(hwnd), c_int(message), c_int(wParam), c_int(lParam))


def createHighlightWin():
	global wndclass, focusHwnd, navigatorHwnd

	wndclass = WNDCLASS()
	wndclass.style = CS_HREDRAW | CS_VREDRAW
	wndclass.lpfnWndProc = WNDPROC(wndProc)
	wndclass.cbClsExtra = wndclass.cbWndExtra = 0
	wndclass.hInstance = windll.kernel32.GetModuleHandleA(c_int(NULL))
	wndclass.hIcon = c_int(NULL)
	wndclass.hCursor = windll.user32.LoadCursorA(c_int(NULL), c_int(IDC_ARROW))
	wndclass.hbrBackground = windll.gdi32.GetStockObject(c_int(transBrush))
	wndclass.lpszMenuName = None
	wndclass.lpszClassName = b"nvdaFh"
	if not windll.user32.RegisterClassA(byref(wndclass)):
		raise WinError()
	hwndParent = gui.mainFrame.GetHandle()
	focusHwnd = createMarkWindow(b"nvdaFh1", hwndParent, focusRect)
	navigatorHwnd = createMarkWindow(b"nvdaFh2", hwndParent, navigatorRect)

	msg = MSG()
	pMsg = pointer(msg)

	while windll.user32.GetMessageA(pMsg, c_int(NULL), 0, 0) != 0:
		windll.user32.TranslateMessage(pMsg)
		windll.user32.DispatchMessageA(pMsg)
		if terminating:
			break

	return msg.wParam


def destroyHighlightWin():
	global wndclass
	windll.user32.DestroyWindow(focusHwnd)
	windll.user32.DestroyWindow(navigatorHwnd)
	while True:
		ret = windll.user32.UnregisterClassA(wndclass.lpszClassName, wndclass.hInstance)
		if ret == 0:
			if GetLastError() == ERROR_CLASS_HAS_WINDOWS:
				time.sleep(0.5)
			else:
				log.error(FormatError())
				break
		else:
			break
	wndclass = None


def startThread():
	global myThread
	myThread = threading.Thread(target=createHighlightWin)
	myThread.daemon = True
	myThread.start()
	#log.debug("focusHighlight started")


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.gdipToken = c_ulong()
		startupInput = GdiplusStartupInput()
		startupInput.GdiplusVersion = 1
		startupOutput = GdiplusStartupOutput()
		gdiplus.GdiplusStartup(byref(self.gdipToken), byref(startupInput), byref(startupOutput))

		wx.CallAfter(startThread)

		def updateStarter():
			def update():
				if terminating:
					return
				if not preparing:
					updateLocations()
				callLater(UPDATE_PERIOD, update)
			callLater(UPDATE_PERIOD, update)

		wx.CallAfter(updateStarter)


	#def getRoleName(self, role):
	#	if role in controlTypes.roleLabels:
	#		return controlTypes.roleLabels[role]
	#	return '%d' % role


	#def getStateName(self, states):
	#	ret = []
	#	for s in states:
	#		if s in controlTypes.stateLabels:
	#			ret.append(controlTypes.stateLabels[s])
	#	return ','.join(ret)


	#def getInfo(self, obj):
	#	return "%s %s %s (%s) (%s)" % (obj.windowClassName, self.getRoleName(obj.role), self.getStateName(obj.states), oleacc.GetRoleText(obj.role), obj.name)


	def event_gainFocus(self, obj, nextHandler):
		global preparing
		preparing = False
		#log.info("gainFocus %s" % self.getInfo(obj))
		updateLocations()
		nextHandler()


	#def event_focusEntered(self, obj, nextHandler):
	#	if obj.windowClassName != 'Scintilla':
	#		log.info("focusEntered %s" % self.getInfo(obj))
	#	nextHandler()


	#def event_becomeNavigatorObject(self, obj, nextHandler, isFocus=None):
	#	log.info("becomeNavigatorObject %s" % self.getInfo(obj))
	#	if obj.windowClassName == 'ComboBox':
	#		updateLocations()
	#	nextHandler()


	def event_stateChange(self, obj, nextHandler):
		#log.info("stateChange %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox':
			updateLocations()
		nextHandler()


	def event_valueChange(self, obj, nextHandler):
		#log.info("valueChange %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox' and obj.role == oleacc.ROLE_SYSTEM_TOOLTIP:
			api.setFocusObject(obj)
			speech.cancelSpeech()
			updateLocations()
		nextHandler()


	#def event_nameChange(self, obj, nextHandler):
	#	log.info("nameChange %s" % self.getInfo(obj))
	#	nextHandler()


	#def event_foreground(self, obj, nextHandler):
	#	log.info("foreground %s" % self.getInfo(obj))
	#	nextHandler()


	def terminate(self):
		global terminating
		terminating = True
		destroyHighlightWin()
		gdiplus.GdiplusShutdown(self.gdipToken)
		#log.debug("focusHighlight terminated")
