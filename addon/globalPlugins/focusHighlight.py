# -*- coding: UTF-8 -*-
# focus highlight
#Copyright (C) 2013-2019 Takuya Nishimoto, Karl-Otto Rosenqvist
# Released under GPL 2

import os
import sys
import threading
import time
from ctypes import (WINFUNCTYPE, FormatError, GetLastError, Structure,
					WinError, byref, c_char, c_char_p, c_float, c_int, c_long,
					c_uint, c_uint32, c_ulong, c_void_p, pointer, windll)
from ctypes.wintypes import BOOL, COLORREF
from io import BytesIO

import addonHandler
import api
import config
import controlTypes
import globalPluginHandler
import globalVars
import gui
import oleacc
import speech
import tones
import ui
import virtualBuffers
import winUser
import wx
from logHandler import log
try:
	from scriptHandler import script
except:
	def script(**kwargs):
		def script_decorator(decoratedScript):
			return decoratedScript
		return script_decorator

from NVDAObjects import NVDAObject

try:
	addonHandler.initTranslation()
except:
	_ = lambda x : x
try:
	ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
	ADDON_PANEL_TITLE = str(ADDON_SUMMARY) if sys.version_info.major >= 3 else unicode(ADDON_SUMMARY)
except:
	ADDON_PANEL_TITLE = ADDON_SUMMARY = 'focusHighlight'
try:
	from gui import SettingsPanel, NVDASettingsDialog, guiHelper
except:
	SettingsPanel = NVDASettingsDialog = guiHelper = None

NULL = 0
SW_HIDE = 0
SW_SHOWNA = 8
WS_POPUP = 0x80000000
WS_DISABLED = 0x8000000
WS_EX_APPWINDOW = 262144
WS_EX_TOOLWINDOW = 128
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 32
CW_USEDEFAULT = 0x80000000
HWND_TOPMOST = -1
SWP_NOACTIVATE = 16
GWL_EXSTYLE = -20
LWA_ALPHA = 0x00000002
LWA_COLORKEY = 0x00000001
WM_DESTROY = 2
WM_PAINT = 15
WM_SHOWWINDOW = 24
WM_TIMER = 275
CS_VREDRAW = 1
CS_HREDRAW = 2
IDC_ARROW = 32512

try:
	from ctypes import POINTER
except:
	from ctypes.wintypes import POINTER

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

config.conf.spec["focusHighlight"] = {
	"passthrough": {
		"defaultMode": "boolean(default=True)",
		"color": "string(min=6, default='2222ff')",
		"dashStyle": "integer(default=2)",
		"thickness": "integer(default=6)",
	},
	"focus": {
		"color": "string(min=6, default='ff0000')",
		"dashStyle": "integer(default=0)",
		"thickness": "integer(default=6)",
	},
	"navigator": {
		"color": "string(min=6, default='00ff00')",
		"dashStyle": "integer(default=3)",
		"thickness": "integer(default=4)",
	}
}

def getConfigARGB(category):
	color = config.conf['focusHighlight'][category]['color']
	r = int(color[0:2], 16)
	g = int(color[2:4], 16)
	b = int(color[4:6], 16)
	return makeARGB(255, r, g, b)

# focus (passthrough)
#ptARGB = makeARGB(255, 0x22, 0x22, 0xff)
#ptDashStyle = 2
#ptThickness = 6

# focus
#fcARGB = makeARGB(255, 0xff, 0x00, 0x00)
#fcDashStyle = 0
#fcThickness = 6

# navigator
#navARGB = makeARGB(255, 0x00, 0xff, 0x00)
#navDashStyle = 3
#navThickness = 4

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
passThroughMode = config.conf['focusHighlight']['passthrough']['defaultMode']
currentAppSleepMode = False
pausePainting = False


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
	return config.conf['focusHighlight']['passthrough']['defaultMode']


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
			argb, dashStyle, thickness, padding = (
				getConfigARGB('passthrough'),
				config.conf['focusHighlight']['passthrough']['dashStyle'],
				config.conf['focusHighlight']['passthrough']['thickness'],
				PADDING_THICK
			)
		else:
			argb, dashStyle, thickness, padding = (
				getConfigARGB('focus'),
				config.conf['focusHighlight']['focus']['dashStyle'],
				config.conf['focusHighlight']['focus']['thickness'],
				PADDING_THICK
			)
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
			argb, dashStyle, thickness, padding = (
				getConfigARGB('navigator'),
				config.conf['focusHighlight']['navigator']['dashStyle'],
				config.conf['focusHighlight']['navigator']['thickness'],
				PADDING_THIN
			)

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
	global passThroughMode, currentAppSleepMode, pausePainting
	passThroughMode = isPassThroughMode()
	currentAppSleepMode = isCurrentAppSleepMode()
	if pausePainting:
		currentAppSleepMode = True
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

	# Translators: Input help mode message
	TOGGLE_DESC = _('Toggles on and off the highlighting of focus')

	@script(
		gesture="kb:NVDA+alt+p",
		description=TOGGLE_DESC,
		category=ADDON_SUMMARY
	)
	def script_togglePainting(self, gesture):
		global pausePainting
		if pausePainting:
			pausePainting = False
			# Translators: togglePainting message
			ui.message(_('{} on').format(ADDON_SUMMARY))
		else:
			pausePainting = True
			# Translators: togglePainting message
			ui.message(_('{} off').format(ADDON_SUMMARY))


	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		if NVDASettingsDialog:
			NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)
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
		if NVDASettingsDialog:
			NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)
		global terminating
		terminating = True
		destroyHighlightWin()
		gdiplus.GdiplusShutdown(self.gdipToken)
		#log.debug("focusHighlight terminated")


if NVDASettingsDialog:

	class AddonSettingsPanel(SettingsPanel):

		title = ADDON_PANEL_TITLE
		dashStyleChoices = (
			# Translators: dash style item
			_("Solid"),
			# Translators: dash style item
			_("Dash"),
			# Translators: dash style item
			_("Dot"),
			# Translators: dash style item
			_("Dash dot"),
			# Translators: dash style item
			_("Dash dot dot"),
		)

		def __init__(self, parent):
			self.beforeRestoreToDefaultsValue = None
			super(AddonSettingsPanel, self).__init__(parent)

		def setWidgetValues(self):
			self.passThroughDefaultModeCheckbox.SetValue(bool(config.conf['focusHighlight']['passthrough']['defaultMode']))
			self.passThroughColorTextCtrl.SetValue(str(config.conf['focusHighlight']['passthrough']['color']))
			self.passThroughThicknessTextCtrl.SetValue(str(config.conf['focusHighlight']['passthrough']['thickness']))
			self.passThroughDashStyleChoice.SetSelection(int(config.conf['focusHighlight']['passthrough']['dashStyle']))
			self.focusColorTextCtrl.SetValue(str(config.conf['focusHighlight']['focus']['color']))
			self.focusThicknessTextCtrl.SetValue(str(config.conf['focusHighlight']['focus']['thickness']))
			self.focusDashStyleChoice.SetSelection(int(config.conf['focusHighlight']['focus']['dashStyle']))
			self.navigatorColorTextCtrl.SetValue(str(config.conf['focusHighlight']['navigator']['color']))
			self.navigatorThicknessTextCtrl.SetValue(str(config.conf['focusHighlight']['navigator']['thickness']))
			self.navigatorDashStyleChoice.SetSelection(int(config.conf['focusHighlight']['navigator']['dashStyle']))

		def saveColor(self, subGroupName, value):
			color = str(value) if sys.version_info.major >= 3 else unicode(value)
			color = color.strip().lower()[:6]
			if len(color) == 3:
				color = color[0] * 2 + color[1] * 2 + color[2] * 2
			valid = True
			try:
				n = int(color, 16)
				# 0x000000 is used for transparent color key
				if n == 0:
					valid = False
			except ValueError:
				valid = False
			if valid and '{:06x}'.format(n) != color:
				valid = False
			if valid:
				config.conf['focusHighlight'][subGroupName]['color'] = color

		def saveThickness(self, subGroupName, value):
			try:
				thickness = int(value)
				if 1 <= thickness <= 30:
					config.conf['focusHighlight'][subGroupName]['thickness'] = thickness
			except ValueError:
				pass

		def saveDashStyle(self, subGroupName, value):
			try:
				value = int(value)
			except ValueError:
				return
			if 0 <= value <= 5:
				config.conf['focusHighlight'][subGroupName]['dashStyle'] = value

		def makeSettings(self, settingsSizer):
			sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
			# Translators: label of a checkbox.
			ptModeText = _("Make focus mode the default")
			self.passThroughDefaultModeCheckbox = sHelper.addItem(wx.CheckBox(self, wx.ID_ANY, label=ptModeText))

			# Translators: focus (in focus mode) panel
			ptGroupText = _("Focus in focus mode")
			ptGroup = guiHelper.BoxSizerHelper(
				parent=self,
				sizer=wx.StaticBoxSizer(parent=self, label=ptGroupText, orient=wx.VERTICAL)
			)
			sHelper.addItem(ptGroup)

			# Translators: label for an edit field.
			colorText = _("Color")
			self.passThroughColorTextCtrl = ptGroup.addLabeledControl(colorText, wx.TextCtrl)
			# Translators: label for an edit field.
			thicknessText = _("Thickness")
			self.passThroughThicknessTextCtrl = ptGroup.addLabeledControl(thicknessText, wx.TextCtrl)
			# Translators: label for an choice field.
			dashStyleText = _("Style")
			self.passThroughDashStyleChoice = ptGroup.addLabeledControl(dashStyleText, wx.Choice, choices=self.dashStyleChoices)

			# Translators: focus (in browse mode) panel
			focusGroupText = _("Focus in browse mode")
			focusGroup = guiHelper.BoxSizerHelper(
				parent=self,
				sizer=wx.StaticBoxSizer(parent=self, label=focusGroupText, orient=wx.VERTICAL)
			)
			sHelper.addItem(focusGroup)

			self.focusColorTextCtrl = focusGroup.addLabeledControl(colorText, wx.TextCtrl)
			self.focusThicknessTextCtrl = focusGroup.addLabeledControl(thicknessText, wx.TextCtrl)
			self.focusDashStyleChoice = focusGroup.addLabeledControl(dashStyleText, wx.Choice, choices=self.dashStyleChoices)

			# Translators: navigator panel
			navGroupText = _("Navigator object")
			navGroup = guiHelper.BoxSizerHelper(
				parent=self,
				sizer=wx.StaticBoxSizer(parent=self, label=navGroupText, orient=wx.VERTICAL)
			)
			sHelper.addItem(navGroup)

			self.navigatorColorTextCtrl = navGroup.addLabeledControl(colorText, wx.TextCtrl)
			self.navigatorThicknessTextCtrl = navGroup.addLabeledControl(thicknessText, wx.TextCtrl)
			self.navigatorDashStyleChoice = navGroup.addLabeledControl(dashStyleText, wx.Choice, choices=self.dashStyleChoices)

			restoreDefaultsButton = sHelper.addItem(
				# Translators: Label of a button.
				wx.Button(self, label=_("Restore defaults"))
			)
			restoreDefaultsButton.Bind(wx.EVT_BUTTON, lambda evt: self.restoreToDefaults())
			self.setWidgetValues()

		def postInit(self):
			self.passThroughDefaultModeCheckbox.SetFocus()

		def onSave(self):
			config.conf['focusHighlight']['passthrough']['defaultMode'] = self.passThroughDefaultModeCheckbox.GetValue()
			self.saveColor('passthrough', self.passThroughColorTextCtrl.GetValue())
			self.saveThickness('passthrough', self.passThroughThicknessTextCtrl.GetValue())
			self.saveDashStyle('passthrough', self.passThroughDashStyleChoice.GetSelection())
			self.saveColor('focus', self.focusColorTextCtrl.GetValue())
			self.saveThickness('focus', self.focusThicknessTextCtrl.GetValue())
			self.saveDashStyle('focus', self.focusDashStyleChoice.GetSelection())
			self.saveColor('navigator', self.navigatorColorTextCtrl.GetValue())
			self.saveThickness('navigator', self.navigatorThicknessTextCtrl.GetValue())
			self.saveDashStyle('navigator', self.navigatorDashStyleChoice.GetSelection())
			# values may be reverted or fixed, so update widgets
			self.setWidgetValues()

		def restoreToDefaults(self):
			self.beforeRestoreToDefaultsValue = (
				config.conf['focusHighlight']['passthrough']['defaultMode'],
				config.conf['focusHighlight']['passthrough']['color'],
				config.conf['focusHighlight']['passthrough']['dashStyle'],
				config.conf['focusHighlight']['passthrough']['thickness'],
				config.conf['focusHighlight']['focus']['color'],
				config.conf['focusHighlight']['focus']['dashStyle'],
				config.conf['focusHighlight']['focus']['thickness'],
				config.conf['focusHighlight']['navigator']['color'],
				config.conf['focusHighlight']['navigator']['dashStyle'],
				config.conf['focusHighlight']['navigator']['thickness']
			)
			config.conf['focusHighlight']['passthrough']['defaultMode'] = True
			config.conf['focusHighlight']['passthrough']['color'] = '2222ff'
			config.conf['focusHighlight']['passthrough']['dashStyle'] = 2
			config.conf['focusHighlight']['passthrough']['thickness'] = 6
			config.conf['focusHighlight']['focus']['color'] = 'ff0000'
			config.conf['focusHighlight']['focus']['dashStyle'] = 0
			config.conf['focusHighlight']['focus']['thickness'] = 6
			config.conf['focusHighlight']['navigator']['color'] = '00ff00'
			config.conf['focusHighlight']['navigator']['dashStyle'] = 3
			config.conf['focusHighlight']['navigator']['thickness'] = 4
			self.setWidgetValues()

		def onDiscard(self):
			if self.beforeRestoreToDefaultsValue:
				config.conf['focusHighlight']['passthrough']['defaultMode'] = self.beforeRestoreToDefaultsValue[0]
				config.conf['focusHighlight']['passthrough']['color'] = self.beforeRestoreToDefaultsValue[1]
				config.conf['focusHighlight']['passthrough']['dashStyle'] = self.beforeRestoreToDefaultsValue[2]
				config.conf['focusHighlight']['passthrough']['thickness'] = self.beforeRestoreToDefaultsValue[3]
				config.conf['focusHighlight']['focus']['color'] = self.beforeRestoreToDefaultsValue[4]
				config.conf['focusHighlight']['focus']['dashStyle'] = self.beforeRestoreToDefaultsValue[5]
				config.conf['focusHighlight']['focus']['thickness'] = self.beforeRestoreToDefaultsValue[6]
				config.conf['focusHighlight']['navigator']['color'] = self.beforeRestoreToDefaultsValue[7]
				config.conf['focusHighlight']['navigator']['dashStyle'] = self.beforeRestoreToDefaultsValue[8]
				config.conf['focusHighlight']['navigator']['thickness'] = self.beforeRestoreToDefaultsValue[9]
