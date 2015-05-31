# focus highlight
# 2015-05-31
# Takuya Nishimoto

import globalPluginHandler
import tones
import wx
import gui
from logHandler import log
import threading
import winUser
import oleacc
import controlTypes
from NVDAObjects.IAccessible import IAccessible
from win32con import (
	NULL,
	CS_HREDRAW,
	CS_VREDRAW,
	CW_USEDEFAULT,
	GWL_STYLE,
	GWL_EXSTYLE,
	HS_BDIAGONAL,
	HS_DIAGCROSS,
	HWND_DESKTOP,
	HWND_TOPMOST,
	IDC_ARROW,
	LWA_COLORKEY,
	LWA_ALPHA,
	SWP_NOACTIVATE,
	SW_SHOWNA,
	WM_PAINT,
	WM_DESTROY,
	WM_SHOWWINDOW,
	WM_TIMER,
	WS_CAPTION,
	WS_DISABLED,
	WS_POPUP,
	WS_VISIBLE,
	WS_EX_APPWINDOW,
	WS_EX_LAYERED,
	WS_EX_TOOLWINDOW,
	WS_EX_TRANSPARENT,
)

import sys
from ctypes import WINFUNCTYPE, Structure, windll
from ctypes import c_long, c_int, c_uint, c_char_p, c_char, byref, pointer
from ctypes import WinError, GetLastError, FormatError
from ctypes.wintypes import COLORREF
import api
import time
import ui

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

def ErrorIfZero(handle):
	if handle == 0:
		raise WinError()
	else:
		return handle

ERROR_CLASS_HAS_WINDOWS = 1412

def RGB(r,g,b):
	return r | (g<<8) | (b<<16)

CreateWindowEx = windll.user32.CreateWindowExA
CreateWindowEx.argtypes = [c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]
CreateWindowEx.restype = ErrorIfZero

# Transparent color key
transColor = COLORREF()
transColor.value = RGB(0xff, 0xff, 0xff)
transBrush = windll.gdi32.CreateSolidBrush(transColor)

brMarkColor = COLORREF()
brMarkColor.value = RGB(0xff, 0x00, 0x00)
brBkColor = COLORREF()
brBkColor.value = RGB(0xff, 0xff, 0xff)
brMarkBrush = windll.gdi32.CreateSolidBrush(brMarkColor)

ptMarkColor = COLORREF()
ptMarkColor.value = RGB(0xff, 0xff, 0xff)
ptBkColor = COLORREF()
ptBkColor.value = RGB(0x00, 0x3f, 0xff)
ptMarkBrush = windll.gdi32.CreateHatchBrush(HS_BDIAGONAL, ptMarkColor)

focusRect = RECT()
focusMarkRectList = [RECT(), RECT(), RECT(), RECT()]
FOCUS_THICKNESS = 4
FOCUS_PADDING = 0
FOCUS_ALPHA = 192
focusHwndList = [0, 0, 0, 0]

navigatorMarkColor = COLORREF()
navigatorMarkColor.value = RGB(0x00, 0x00, 0xff)
navBkColor = COLORREF()
navBkColor.value = RGB(0x00, 0xff, 0x00)
navigatorMarkBrush = windll.gdi32.CreateHatchBrush(HS_DIAGCROSS, navigatorMarkColor)

navigatorRect = RECT()
navigatorMarkRectList = [RECT(), RECT(), RECT(), RECT()]
NAVIGATOR_THICKNESS = 4
NAVIGATOR_PADDING = 4
NAVIGATOR_ALPHA = 192
navigatorHwndList = [0, 0, 0, 0]

ID_TIMER = 100
UPDATE_PERIOD = 300

wndclass = None
preparing = True
terminating = False

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


def setMarkPositions(marks, region, thickness, padding=0):
	marks[0].top    = region.top - thickness - padding
	marks[0].bottom = region.top - padding
	marks[0].left   = region.left - padding
	marks[0].right  = region.right + padding

	marks[1].top    = region.bottom + padding
	marks[1].bottom = region.bottom + thickness + padding
	marks[1].left   = region.left - padding
	marks[1].right  = region.right + padding

	marks[2].top    = region.top - thickness - padding
	marks[2].bottom = region.bottom + thickness + padding
	marks[2].left   = region.left - thickness - padding
	marks[2].right  = region.left - padding

	marks[3].top    = region.top - thickness - padding
	marks[3].bottom = region.bottom + thickness + padding
	marks[3].left   = region.right + padding
	marks[3].right  = region.right + thickness + padding


def moveAndShowWindow(hwnd, rect):
	if not hwnd: return
	left = rect.left
	top = rect.top
	width = rect.right - left
	height = rect.bottom - top
	windll.user32.ShowWindow(c_int(hwnd), winUser.SW_HIDE)
	windll.user32.MoveWindow(c_int(hwnd), left, top, width, height, True)
	windll.user32.ShowWindow(c_int(hwnd), SW_SHOWNA)


def limitRectInDesktop(newRect):
	l, t, w, h = api.getDesktopObject().location
	newRect.top = max(0, newRect.top)
	newRect.left = max(0, newRect.left)
	newRect.right = max(0, min(l+w, newRect.right))
	newRect.bottom = max(0, min(t+h, newRect.bottom))
	return newRect


def locationAvailable(obj):
	return (obj and hasattr(obj, 'location') and obj.location and len(obj.location) >= 4)

def isPassThroughMode():
	try:
		# until 2014.4
		import virtualBuffers
		if hasattr(virtualBuffers, "reportPassThrough"):
			return browseMode.reportPassThrough.last
		# since 2015.1
		import browseMode
		return browseMode.reportPassThrough.last
	except:
		return False

def updateFocusLocation(sender=None):
	global focusRect
	if locationAvailable(sender):
		newRect = location2rect(sender.location)
	elif locationAvailable(api.getFocusObject()):
		newRect = location2rect(api.getFocusObject().location)
	else:
		return
	newRect = limitRectInDesktop(newRect)
	if not rectEquals(newRect, focusRect):
		focusRect = newRect
		setMarkPositions(focusMarkRectList, focusRect, FOCUS_THICKNESS, FOCUS_PADDING)
		for i in xrange(4):
			moveAndShowWindow(focusHwndList[i], focusMarkRectList[i])


def updateNavigatorLocation():
	global navigatorRect
	nav = api.getNavigatorObject()
	if locationAvailable(nav):
		newRect = location2rect(nav.location)
	elif locationAvailable(api.getFocusObject()):
		newRect = location2rect(api.getFocusObject().location)
	else:
		return
	newRect = limitRectInDesktop(newRect)
	if not rectEquals(newRect, navigatorRect):
		navigatorRect = newRect
		setMarkPositions(navigatorMarkRectList, navigatorRect, NAVIGATOR_THICKNESS, NAVIGATOR_PADDING)
		for i in xrange(4):
			moveAndShowWindow(navigatorHwndList[i], navigatorMarkRectList[i])


def createMarkWindow(wndclass, name, hwndParent, rect, alpha):
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
	left = rect.left
	top = rect.top
	width = rect.right - left
	height = rect.bottom - top
	windll.user32.SetWindowPos(c_int(hwnd), HWND_TOPMOST, left, top, width, height, SWP_NOACTIVATE)
	exstyle = windll.user32.GetWindowLongA(c_int(hwnd), GWL_EXSTYLE)
	exstyle &= ~WS_EX_APPWINDOW
	exstyle |= WS_EX_TOOLWINDOW | WS_EX_LAYERED | WS_EX_TRANSPARENT
	windll.user32.SetWindowLongA(c_int(hwnd), GWL_EXSTYLE, exstyle)
	windll.user32.SetLayeredWindowAttributes(c_int(hwnd), byref(transColor), alpha, (LWA_ALPHA | LWA_COLORKEY))
	return hwnd


def doPaint(hwnd):
	if rectEquals(focusRect, navigatorRect) or hwnd in focusHwndList:
		if isPassThroughMode():
			color, brush, bkColor = ptMarkColor, ptMarkBrush, ptBkColor
		else:
			color, brush, bkColor = brMarkColor, brMarkBrush, brBkColor
	elif hwnd in navigatorHwndList:
		color, brush, bkColor = navigatorMarkColor, navigatorMarkBrush, navBkColor
	else:
		return
	ps = PAINTSTRUCT()
	rect = RECT()
	hdc = windll.user32.BeginPaint(c_int(hwnd), byref(ps))
	windll.gdi32.SetDCBrushColor(c_int(hdc), color)
	windll.gdi32.SetBkColor(c_int(hdc), bkColor)
	windll.user32.GetClientRect(c_int(hwnd), byref(rect))
	windll.user32.FillRect(hdc, byref(rect), brush)
	windll.user32.EndPaint(c_int(hwnd), byref(ps))


def invalidateRects():
	for hwnd in focusHwndList + navigatorHwndList:
		if hwnd:
			windll.user32.InvalidateRect(c_int(hwnd), None, True)


def wndProc(hwnd, message, wParam, lParam):
	if message == WM_PAINT:
		doPaint(hwnd)
		return 0
	elif message == WM_DESTROY:
		windll.user32.PostQuitMessage(0)
		return 0
	elif message == WM_SHOWWINDOW:
		timer = windll.user32.SetTimer(c_int(hwnd), ID_TIMER, UPDATE_PERIOD, None)
		return 0
	elif message == WM_TIMER:
		if preparing:
			return 0
		updateFocusLocation()
		try:
			updateNavigatorLocation()
		except:
			pass
		invalidateRects()
		return 0
	return windll.user32.DefWindowProcA(c_int(hwnd), c_int(message), c_int(wParam), c_int(lParam))


def createHighlightWin():
	global wndclass
	wndclass = WNDCLASS()
	wndclass.style = CS_HREDRAW | CS_VREDRAW
	wndclass.lpfnWndProc = WNDPROC(wndProc)
	wndclass.cbClsExtra = wndclass.cbWndExtra = 0
	wndclass.hInstance = windll.kernel32.GetModuleHandleA(c_int(NULL))
	wndclass.hIcon = c_int(NULL)
	wndclass.hCursor = windll.user32.LoadCursorA(c_int(NULL), c_int(IDC_ARROW))
	wndclass.hbrBackground = windll.gdi32.GetStockObject(c_int(transBrush))
	wndclass.lpszMenuName = None
	wndclass.lpszClassName = "nvdaFh"
	if not windll.user32.RegisterClassA(byref(wndclass)):
		raise WinError()
	hwndParent = gui.mainFrame.GetHandle()
	for i in xrange(4):
		focusHwndList[i] = createMarkWindow(wndclass, "nvdaFh" + str(i+1), hwndParent, focusMarkRectList[i], FOCUS_ALPHA)

	for i in xrange(4):
		navigatorHwndList[i] = createMarkWindow(wndclass, "nvdaFh" + str(i+5), hwndParent, navigatorMarkRectList[i], NAVIGATOR_ALPHA)

	msg = MSG()
	pMsg = pointer(msg)

	while windll.user32.GetMessageA(pMsg, c_int(NULL), 0, 0) != 0:
		try:
			windll.user32.TranslateMessage(pMsg)
			windll.user32.DispatchMessageA(pMsg)
		except Exception as e:
			log.debug(unicode(e))
		if terminating:
			break
	return msg.wParam


def destroyHighlightWin():
	global wndclass
	for i in xrange(4):
		windll.user32.DestroyWindow(focusHwndList[i])
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
	log.debug("focusHighlight started")


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		wx.CallAfter(startThread)
		
	def getRoleName(self, role):
		if role in controlTypes.roleLabels:
			return controlTypes.roleLabels[role]
		return '%d' % role

	def getStateName(self, states):
		ret = []
		for s in states:
			if s in controlTypes.stateLabels:
				ret.append(controlTypes.stateLabels[s])
		return ','.join(ret)
		
	def getInfo(self, obj):
		return "%s %s %s (%s) (%s)" % (obj.windowClassName, self.getRoleName(obj.role), self.getStateName(obj.states), oleacc.GetRoleText(obj.role), obj.name)

	def event_gainFocus(self, obj, nextHandler):
		global preparing
		preparing = False
		log.info("gainFocus %s" % self.getInfo(obj))
 		updateFocusLocation(obj)
		updateNavigatorLocation()
		nextHandler()

	def event_focusEntered(self, obj, nextHandler):
		if obj.windowClassName != 'Scintilla':
			log.info("focusEntered %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboLBox':
			self.ComboLBox = obj
		nextHandler()

	def event_becomeNavigatorObject(self, obj, nextHandler):
		log.info("becomeNavigatorObject %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox':
			updateFocusLocation(obj)
			updateNavigatorLocation()
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		log.info("stateChange %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox':
			updateFocusLocation(obj)
			updateNavigatorLocation()
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		log.info("valueChange %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox' and obj.role == oleacc.ROLE_SYSTEM_TOOLTIP:
			updateFocusLocation(obj)
			updateNavigatorLocation()
			api.setFocusObject(obj)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		log.info("nameChange %s" % self.getInfo(obj))
		nextHandler()

	def event_foreground(self, obj, nextHandler):
		log.info("foreground %s" % self.getInfo(obj))
		nextHandler()

	def terminate(self):
		global terminating
		terminating = True
		destroyHighlightWin()
		log.info("focusHighlight terminated")
