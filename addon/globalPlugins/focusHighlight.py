# focus highlight
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
from ctypes import c_long, c_int, c_uint, c_char_p, c_char, byref, pointer, POINTER, sizeof
from ctypes import WinError, GetLastError, FormatError
from ctypes.wintypes import COLORREF
import api
import time
import ui
import speech
import virtualBuffers
import windowUtils

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

class MONITORINFO(Structure):
	_fields_ = [('cbSize', c_int),   # DWORD
				('rcMonitor', RECT), # RECT
				('rcWork', RECT),    # RECT
				('dwFlags', c_int)]  # DWORD

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
TRANS_ALPHA = 0

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

focusObject = navObject = None
focusFixDpiMode = navigatorFixDpiMode = 0

ID_TIMER = 100
UPDATE_PERIOD = 300

wndclass = None
preparing = True
terminating = False
passThroughMode = False
currentAppSleepMode = False

def rectEquals(r1, r2):
	return (r1.top == r2.top and r1.bottom == r2.bottom and r1.left == r2.left and r1.right == r2.right)

def getDpiInfo(obj, hmon):
	pt = POINT()
	pt.x = 0
	pt.y = 0
	hprimon = windll.user32.MonitorFromPoint(pt, 0)
	pmScale = 0.01 * getMonitorScaleFactor(hprimon)
	scale = 0.01 * getMonitorScaleFactor(hmon)
	try:
		dpiForSystem = windll.user32.GetDpiForSystem()
	except AttributeError:
		return 0, 96, 96, scale
	if not hasattr(obj, 'windowHandle'):
		return 0, dpiForSystem, dpiForSystem, scale
	wh = obj.windowHandle
	wdac = (0x0f & windll.user32.GetWindowDpiAwarenessContext(wh))
	dpiForWindow = windll.user32.GetDpiForWindow(wh)

	appName = obj.appModule.appName
	wc = obj.windowClassName

	newScale = float(dpiForSystem) / dpiForWindow if dpiForWindow > 0 else 1.0
	if wdac == 0:
		newScale = 1.0
		log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
	elif wdac == 1:
		if obj.role in (oleacc.ROLE_SYSTEM_MENUPOPUP, oleacc.ROLE_SYSTEM_MENUITEM) or wc == '#32768':
			newScale = pmScale
			#log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
		else:
			newScale = 1.0
			#log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
	elif wdac == 2:
		if appName == 'iexplore':
			pass
		elif appName == 'explorer':
			if wc == 'DirectUIHWND':
				newScale = 1.0
				log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
		elif wc == 'Edit' or wc == 'VirtualConsoleClass' or wc == 'ConsoleWindowClass':
			newScale = 1.0
			log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
		elif obj.role in (oleacc.ROLE_SYSTEM_MENUPOPUP, oleacc.ROLE_SYSTEM_MENUITEM) or wc == '#32768':
			newScale = pmScale
			#log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
	else:
		log.debug('ac %d %s %s scale %f newScale %f' % (wdac, appName, wc, scale, newScale))
	return wdac, dpiForWindow, dpiForSystem, newScale

def getMonitorScaleFactor(hmon):
	scaleFactor = c_int()
	try:
		hResult = windll.shcore.GetScaleFactorForMonitor(hmon, byref(scaleFactor))
	except WindowsError:
		return 100
	if hResult != 0:
		log.warning('GetScaleFactorForMonitor (not S_OK) %x' % hResult)
	return scaleFactor.value

def getMonInfo(obj):
	if locationAvailable(obj):
		left, top, width, height = obj.location
		pt = POINT()
		pt.x = left + width / 2
		pt.y = top + height / 2
		hmon = windll.user32.MonitorFromPoint(pt, 0)
	else:
		hmon = windll.user32.MonitorFromWindow(obj.windowHandle, 0)
	monInfo = MONITORINFO()
	monInfo.cbSize = sizeof(MONITORINFO)
	bResult = windll.user32.GetMonitorInfoA(hmon, byref(monInfo))
	if bResult == 0:
		log.warning('GetMonitorInfoA error %x' % GetLastError())
	# current monitor DPI
	# https://msdn.microsoft.com/en-us/library/windows/desktop/dn280510(v=vs.85).aspx
	dpiX = c_int()
	dpiY = c_int()
	try:
		hResult = windll.shcore.GetDpiForMonitor(hmon, 0, byref(dpiX), byref(dpiY))
	except WindowsError:
		return monInfo, 96, 96, hmon
	if hResult != 0:
		log.warning('GetDpiForMonitor (not S_OK) %x' % hResult)
	return monInfo, dpiX.value, dpiY.value, hmon

def getMonPos(monInfo, dpiX, dpiY):
	ml = int(monInfo.rcMonitor.left)
	mt = int(monInfo.rcMonitor.top)
	mr = int(monInfo.rcMonitor.right)
	mb = int(monInfo.rcMonitor.bottom)
	#if dpiX > 0:
	#	ml = int(ml * 96.0 / dpiX)
	#	mr = int(mr * 96.0 / dpiX)
	#if dpiY > 0:
	#	mt = int(mt * 96.0 / dpiY)
	#	mb = int(mb * 96.0 / dpiY)
	return ml, mt, mr, mb

def objToRect(obj):
	location = obj.location
	rect = RECT()
	if not (location and len(location) >= 4):
		return rect
	monInfo, dpiX, dpiY, hmon = getMonInfo(obj)
	monLeft, monTop, monRight, monBottom = getMonPos(monInfo, dpiX, dpiY)
	wdac, dpiForWindow, dpiForSystem, scale = getDpiInfo(obj, hmon)
	left, top, width, height = location
	leftInMon = left
	topInMon = top
	if wdac == 0:
		leftInMon -= monLeft
		topInMon  -= monTop
	#scale = float(dpiForSystem) / float(dpiForWindow) if dpiForWindow > 0 else 1
	leftInMon *= scale
	topInMon *= scale
	width *= scale
	height *= scale
	rect.left = int(leftInMon)
	rect.top  = int(topInMon)
	if wdac == 0:
		rect.left += int(monLeft)
		rect.top += int(monTop)
	rect.right = int(rect.left + width)
	rect.bottom = int(rect.top + height)
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

#def doFixLocation(left, top, right, bottom, dpiAC=0, dpiForWindow=96.0, dpiForSystem=96.0):
#	if dpiAC == 2:
#		scale = dpiForSystem / dpiForWindow
#		left = int(left * scale)
#		top = int(top * scale)
#		right = int(right * scale)
#		bottom = int(bottom * scale)
#	return left, top, right, bottom

def moveAndShowWindow(hwnd, rect):
	if not hwnd: return
	left = rect.left
	top = rect.top
	right = rect.right
	bottom = rect.bottom
	left, top, right, bottom = limitRectInDesktop(left, top, right, bottom)
	width = right - left
	height = bottom - top
	windll.user32.ShowWindow(c_int(hwnd), winUser.SW_HIDE)
	windll.user32.MoveWindow(c_int(hwnd), left, top, width, height, True)
	windll.user32.ShowWindow(c_int(hwnd), SW_SHOWNA)


def limitRectInDesktop(left, top, right, bottom):
	l = windll.user32.GetSystemMetrics(76) # SM_XVIRTUALSCREEN: left side of the virtual screen
	t = windll.user32.GetSystemMetrics(77) # SM_YVIRTUALSCREEN: top of the virtual screen
	w = windll.user32.GetSystemMetrics(78) # SM_CXVIRTUALSCREEN: width of the virtual screen in pixels
	h = windll.user32.GetSystemMetrics(79) # SM_CYVIRTUALSCREEN: height of the virtual screen in pixels
	r = l+w
	b = t+h
	left = max(l, left)
	top = max(t, top)
	right = min(r, right)
	bottom = min(b, bottom)
	return left, top, right, bottom


def locationAvailable(obj):
	return (obj and hasattr(obj, 'location') and obj.location and len(obj.location) >= 4)

def isPassThroughMode():
	focus = api.getFocusObject()
	if hasattr(focus, 'treeInterceptor') and focus.treeInterceptor:
		return focus.treeInterceptor.passThrough
	return False

def isCurrentAppSleepMode():
	focus = api.getFocusObject()
	if hasattr(focus, 'appModule') and focus.appModule:
		return focus.appModule.sleepMode
	return False

def updateFocusLocation():
	global focusRect, focusFixDpiMode, focusObject
	focus = api.getFocusObject()
	if locationAvailable(focus):
		newRect = objToRect(focus)
	else:
		return
	focusObject = focus
	#focusFixDpiMode, dpiForWindow, dpiForSystem = getDpiInfo(focus)
	#newRect = limitRectInDesktop(newRect, focusFixDpiMode, dpiForWindow, dpiForSystem)
	if not rectEquals(newRect, focusRect):
		focusRect = newRect
		setMarkPositions(focusMarkRectList, focusRect, FOCUS_THICKNESS, FOCUS_PADDING)
		for i in xrange(4):
			moveAndShowWindow(focusHwndList[i], focusMarkRectList[i])


def updateNavigatorLocation():
	global navigatorRect, navigatorFixDpiMode, navObject
	try:
		nav = api.getNavigatorObject()
	except:
		return
	if locationAvailable(nav):
		newRect = objToRect(nav)
	elif locationAvailable(api.getFocusObject()):
		newRect = objToRect(api.getFocusObject())
	else:
		return
	navObject = nav
	#navigatorFixDpiMode, dpiForWindow, dpiForSystem = getDpiInfo(nav)
	#newRect = limitRectInDesktop(newRect, navigatorFixDpiMode, dpiForWindow, dpiForSystem)
	if not rectEquals(newRect, navigatorRect):
		navigatorRect = newRect
		setMarkPositions(navigatorMarkRectList, navigatorRect, NAVIGATOR_THICKNESS, NAVIGATOR_PADDING)
		for i in xrange(4):
			moveAndShowWindow(navigatorHwndList[i], navigatorMarkRectList[i])


def createMarkWindow(name, hwndParent, rect, alpha):
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
	left = rect.left
	top = rect.top
	right = rect.right
	bottom = rect.bottom
	#left, top, right, bottom = doFixLocation(left, top, right, bottom, dpiAC, dpiForWindow, dpiForSystem)
	width = right - left
	height = bottom - top
	windll.user32.SetWindowPos(c_int(hwnd), HWND_TOPMOST, left, top, width, height, SWP_NOACTIVATE)
	exstyle = windll.user32.GetWindowLongA(c_int(hwnd), GWL_EXSTYLE)
	exstyle &= ~WS_EX_APPWINDOW
	exstyle |= WS_EX_TOOLWINDOW | WS_EX_LAYERED | WS_EX_TRANSPARENT
	windll.user32.SetWindowLongA(c_int(hwnd), GWL_EXSTYLE, exstyle)
	windll.user32.SetLayeredWindowAttributes(c_int(hwnd), byref(transColor), alpha, (LWA_ALPHA | LWA_COLORKEY))
	return hwnd


def doPaint(hwnd):
	if currentAppSleepMode:	
		color, brush, bkColor, alpha = transColor, transBrush, transColor, TRANS_ALPHA
	elif rectEquals(focusRect, navigatorRect) or hwnd in focusHwndList:
		if passThroughMode:
			color, brush, bkColor, alpha = ptMarkColor, ptMarkBrush, ptBkColor, FOCUS_ALPHA
		else:
			color, brush, bkColor, alpha = brMarkColor, brMarkBrush, brBkColor, FOCUS_ALPHA
	elif hwnd in navigatorHwndList:
		color, brush, bkColor, alpha = navigatorMarkColor, navigatorMarkBrush, navBkColor, NAVIGATOR_ALPHA
	else:
		return
	windll.user32.SetLayeredWindowAttributes(c_int(hwnd), 0, alpha, LWA_ALPHA)
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
	global passThroughMode, currentAppSleepMode
	if message == WM_PAINT:
		doPaint(hwnd)
		return 0
	elif message == WM_DESTROY:
		windll.user32.PostQuitMessage(0)
		return 0
	elif message == WM_SHOWWINDOW:
		if hwnd == focusHwndList[0]:
			timer = windll.user32.SetTimer(c_int(hwnd), ID_TIMER, UPDATE_PERIOD, None)
		return 0
	elif message == WM_TIMER:
		if not preparing and hwnd == focusHwndList[0]:
			updateFocusLocation()
			updateNavigatorLocation()
			invalidateRects()
			passThroughMode = isPassThroughMode()
			currentAppSleepMode = isCurrentAppSleepMode()
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
	#dpiAC, dpiForWindow, dpiForSystem = getDpiInfo(focusObject)
	for i in xrange(4):
		focusHwndList[i] = createMarkWindow("nvdaFh" + str(i+1), hwndParent, focusMarkRectList[i], FOCUS_ALPHA)
	#dpiAC, dpiForWindow, dpiForSystem = getDpiInfo(navObject)
	for i in xrange(4):
		navigatorHwndList[i] = createMarkWindow("nvdaFh" + str(i+5), hwndParent, navigatorMarkRectList[i], NAVIGATOR_ALPHA)

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
		#if obj.appModule.appName != 'notepad': return None
		if obj.appModule:
			s = '(app %s) ' % obj.appModule.appName
		else:
			s = ''
		s += "(wc %s)" % obj.windowClassName
		rect = None
		if locationAvailable(obj):
			rect = objToRect(obj)
		if rect:
			s += ' (rect pos %d %d size %d %d)' % (rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
			#px, py = windowUtils.logicalToPhysicalPoint(obj.windowHandle, rect.left, rect.top)
			#s += ' (phys pos %d %d)' % (px, py)
			#lx, ly = windowUtils.physicalToLogicalPoint(obj.windowHandle, rect.left, rect.top)
			#s += ' (logi pos %d %d)' % (lx, ly)
		monInfo, dpiX, dpiY, hmon = getMonInfo(obj)
		wdac, dpiForWindow, dpiForSystem, scale = getDpiInfo(obj, hmon)
		s += ' (dpi ac %d win %d sys %d scale %.2f)' % (wdac, dpiForWindow, dpiForSystem, scale)
		ml, mt, mr, mb = getMonPos(monInfo, dpiX, dpiY)
		s += ' (mon pos %d %d size %d %d)' % (
			ml, mt,
			mr - ml,
			mb - mt
		)
		if rect:
			s += ' (posInMon %d %d)' % (
				rect.left   - ml,
				rect.top    - mt
			)
		#s += ' (workRect %d %d %d %d)' % (
		#	monInfo.rcWork.left,
		#	monInfo.rcWork.top,
		#	monInfo.rcWork.right,
		#	monInfo.rcWork.bottom
		#)
		s += ' (primary %d)' % monInfo.dwFlags
		s += ' (dpiMon %d %d)' % (dpiX, dpiY)
		# available monitors
		cmon = windll.user32.GetSystemMetrics(80) # SM_CMONITORS
		s += ' (cMon %d)' % cmon
		s += " (role %s state %s roletext %s)" % (self.getRoleName(obj.role), self.getStateName(obj.states), oleacc.GetRoleText(obj.role))
		if obj.name:
			s += " (name %s)" % obj.name
		return s

	def event_gainFocus(self, obj, nextHandler):
		global preparing
		preparing = False
		s = self.getInfo(obj)
		if s:
			log.debug(s)
 		updateFocusLocation()
		updateNavigatorLocation()
		invalidateRects()
		nextHandler()

	#def event_focusEntered(self, obj, nextHandler):
	#	if obj.windowClassName != 'Scintilla':
	#		log.info("focusEntered %s" % self.getInfo(obj))
	#	nextHandler()

	#def event_becomeNavigatorObject(self, obj, nextHandler):
	#	log.info("becomeNavigatorObject %s" % self.getInfo(obj))
	#	if obj.windowClassName == 'ComboBox':
	#		updateFocusLocation(obj)
	#		updateNavigatorLocation()
	#	nextHandler()

	def event_stateChange(self, obj, nextHandler):
		#log.info("stateChange %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox':
			updateFocusLocation()
			updateNavigatorLocation()
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		#log.info("valueChange %s" % self.getInfo(obj))
		if obj.windowClassName == 'ComboBox' and obj.role == oleacc.ROLE_SYSTEM_TOOLTIP:
			api.setFocusObject(obj)
			speech.cancelSpeech()
			updateFocusLocation()
			updateNavigatorLocation()
			invalidateRects()
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
		log.debug("focusHighlight terminated")
