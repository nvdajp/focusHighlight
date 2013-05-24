# highlight.py
# Takuya Nishimoto

import globalPluginHandler
import tones
import wx
import gui
from logHandler import log
import threading
import winUser
from NVDAObjects.IAccessible import IAccessible
import win32con
import sys
from ctypes import WINFUNCTYPE, Structure, windll
from ctypes import c_long, c_int, c_uint, c_char_p, c_char, byref, pointer
from ctypes.wintypes import COLORREF

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

HWND_TOPMOST = -1
SWP_NOACTIVATE = 0x0010
GWL_EXSTYLE = -20
SW_SHOWNA = 8
WS_EX_TOOLWINDOW = 0x00000080
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 0x00000020
WS_EX_APPWINDOW = 0x00040000
LWA_COLORKEY = 0x00000001
LWA_ALPHA = 0x00000002

def RGB(r,g,b):
	return r | (g<<8) | (b<<16)

CreateWindowEx = windll.user32.CreateWindowExA
CreateWindowEx.argtypes = [c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]
CreateWindowEx.restype = ErrorIfZero

# Transparent color key
TRANS_COLORREF = COLORREF()
TRANS_COLORREF.value = RGB(0xff, 0xff, 0xff)
trans_brush = windll.gdi32.CreateSolidBrush(TRANS_COLORREF)

highlight_color = COLORREF()
highlight_color.value = RGB(0xff, 0x00, 0x00)
highlight_brush = windll.gdi32.CreateSolidBrush(highlight_color)

focusRect = RECT()
highlightRectList = [RECT(), RECT(), RECT(), RECT()]
THICKNESS = 4
alpha = 192
hwndFocusList = [0, 0, 0, 0]

def onFocusChangedEvent(sender):
	global focusRect
	if not (isinstance(sender, IAccessible) and hasattr(sender, 'location')):
		return
	newRect = RECT()
	newRect.left = sender.location[0]
	newRect.top = sender.location[1]
	newRect.right = newRect.left + sender.location[2]
	newRect.bottom = newRect.top + sender.location[3]
	if newRect.top != focusRect.top or newRect.bottom != focusRect.bottom or newRect.left != focusRect.left or newRect.right != focusRect.right:
		highlightRectList[0].top    = newRect.top - THICKNESS
		highlightRectList[0].bottom = newRect.top
		highlightRectList[0].left   = newRect.left
		highlightRectList[0].right  = newRect.right
		highlightRectList[1].top    = newRect.bottom
		highlightRectList[1].bottom = newRect.bottom + THICKNESS
		highlightRectList[1].left   = newRect.left
		highlightRectList[1].right  = newRect.right
		highlightRectList[2].top    = newRect.top - THICKNESS
		highlightRectList[2].bottom = newRect.bottom + THICKNESS
		highlightRectList[2].left   = newRect.left - THICKNESS
		highlightRectList[2].right  = newRect.left
		highlightRectList[3].top    = newRect.top - THICKNESS
		highlightRectList[3].bottom = newRect.bottom + THICKNESS
		highlightRectList[3].left   = newRect.right
		highlightRectList[3].right  = newRect.right + THICKNESS
		for i in xrange(4):
			hwnd = hwndFocusList[i]
			if hwnd:
				left = highlightRectList[i].left
				top = highlightRectList[i].top
				width = highlightRectList[i].right - left
				height = highlightRectList[i].bottom - top
				windll.user32.ShowWindow(c_int(hwnd), winUser.SW_HIDE)
				windll.user32.MoveWindow(c_int(hwnd), left, top, width, height, True)
				windll.user32.ShowWindow(c_int(hwnd), SW_SHOWNA)
	
def HighlightWin():
	global hwndFocusFocusList
	wndclass = WNDCLASS()
	wndclass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
	wndclass.lpfnWndProc = WNDPROC(WndProc)
	wndclass.cbClsExtra = wndclass.cbWndExtra = 0
	wndclass.hInstance = windll.kernel32.GetModuleHandleA(c_int(win32con.NULL))
	wndclass.hIcon = c_int(win32con.NULL)
	wndclass.hCursor = windll.user32.LoadCursorA(c_int(win32con.NULL), c_int(win32con.IDC_ARROW))
	wndclass.hbrBackground = windll.gdi32.GetStockObject(c_int(trans_brush))
	wndclass.lpszMenuName = None
	wndclass.lpszClassName = "HighlightWin"
	if not windll.user32.RegisterClassA(byref(wndclass)):
		raise WinError()
	hwndHide = CreateWindowEx(0,
							  wndclass.lpszClassName,
							  "HighlightWin0",
							  win32con.WS_POPUP,
							  win32con.CW_USEDEFAULT,
							  win32con.CW_USEDEFAULT,
							  win32con.CW_USEDEFAULT,
							  win32con.CW_USEDEFAULT,
							  win32con.HWND_DESKTOP,
							  win32con.NULL,
							  wndclass.hInstance,
							  win32con.NULL)
	for i in xrange(4):
		hwnd = CreateWindowEx(0,
							  wndclass.lpszClassName,
							  "HighlightWin" + str(i+1),
							  win32con.WS_POPUP|win32con.WS_VISIBLE,
							  win32con.CW_USEDEFAULT,
							  win32con.CW_USEDEFAULT,
							  win32con.CW_USEDEFAULT,
							  win32con.CW_USEDEFAULT,
							  hwndHide,
							  win32con.NULL,
							  wndclass.hInstance,
							  win32con.NULL)
		left = highlightRectList[i].left
		top = highlightRectList[i].top
		width = highlightRectList[i].right - left
		height = highlightRectList[i].bottom - top
		windll.user32.SetWindowPos(c_int(hwnd), HWND_TOPMOST, left, top, width, height, SWP_NOACTIVATE)
		style = windll.user32.GetWindowLongA(c_int(hwnd), GWL_EXSTYLE)
		style &= ~WS_EX_APPWINDOW
		style = style | WS_EX_TOOLWINDOW | WS_EX_LAYERED | WS_EX_TRANSPARENT
		windll.user32.SetWindowLongA(c_int(hwnd), GWL_EXSTYLE, style)
		windll.user32.SetLayeredWindowAttributes(c_int(hwnd), byref(TRANS_COLORREF), alpha, (LWA_ALPHA | LWA_COLORKEY))
		hwndFocusList[i] = hwnd

	msg = MSG()
	pMsg = pointer(msg)
	NULL = c_int(win32con.NULL)

	while windll.user32.GetMessageA(pMsg, NULL, 0, 0) != 0:
		windll.user32.TranslateMessage(pMsg)
		windll.user32.DispatchMessageA(pMsg)

	for i in xrange(4):
		windll.user32.DestroyWindow(hwndFocusList[i])
	windll.user32.DestroyWindow(hwndHide)
	windll.user32.UnregisterClassA(byref(wndclass), wndclass.hInstance)
	return msg.wParam

ID_TIMER = 100

def WndProc(hwnd, message, wParam, lParam):
	if message == win32con.WM_PAINT:
		ps = PAINTSTRUCT()
		rect = RECT()
		hdc = windll.user32.BeginPaint(c_int(hwnd), byref(ps))
		windll.gdi32.SetDCBrushColor(c_int(hdc), highlight_color)
		windll.user32.GetClientRect(c_int(hwnd), byref(rect))
		windll.user32.FillRect(hdc, byref(rect), highlight_brush)
		windll.user32.EndPaint(c_int(hwnd), byref(ps))
		return 0
	elif message == win32con.WM_DESTROY:
		windll.user32.PostQuitMessage(0)
		return 0
	elif message == win32con.WM_SHOWWINDOW:
		timer = windll.user32.SetTimer(c_int(hwnd), ID_TIMER, 300, None)
		return 0
	elif message == win32con.WM_TIMER:
		for hwnd in hwndFocusList:
			if hwnd:
				windll.user32.InvalidateRect(c_int(hwnd), None, True)
		return 0

	return windll.user32.DefWindowProcA(c_int(hwnd), c_int(message), c_int(wParam), c_int(lParam))

class Highlighter(object):
	def run(self):
		t = threading.Thread(target=self._bg)
		t.daemon = True
		t.start()
	def _bg(self):
		HighlightWin()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	global highlighter
	highlighter = Highlighter()
	highlighter.run()

	def event_gainFocus(self, obj, nextHandler):
		onFocusChangedEvent(obj)
		nextHandler()
