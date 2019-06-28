# Focus Highlight #

* 저자: Takuya Nishimoto
* Download [안정 버전][2]
* Download [개발 버전][1]

이 추가 기능은 NVDA navigator 객체와 초점이 있는 객체/컨트롤의 위치를 색깔 있는 사각형으로 강조 표시합니다. 시각 장애인
사용자, 시각 장애인 교육자, 또는 개발자에게 유용합니다.

다음의 2 색이 이 추가 기능에 의해 사용됩니다:

* NVDA가 브라우즈 모드에 있을 때에는 navigator 객체에 가느다란 녹색 일점쇄선으로 직사각형이 표시됩니다.
* NVDA가 브라우즈 모드에 있을 때에는 포커스가 위치한 객체에 가느다란 빨간색 직사각형이 표시됩니다.
* NVDA가 브라우즈 모드에 있을 때에는 navigator 객체에 포커스가 위치했을 때 굵은 빨간색 직사각형이 표시됩니다.
* NVDA가 포커스 모드에 있을 때, 즉 키 입력이 조작 장치에 전달될 때에는 굵은 파란색 점선으로 직사각형이 표시됩니다.

객체 추적을 중단하려면 애드온을 비활성화하거나 삭제하세요.

NVDA 설정 창에 대한 Focus Highlight 분류가 있을 경우, 다음 항목들을 사용할 수 있습니다.

* Make focus mode the default: This checkbox is enabled by default. When it
  is unchecked, this add-on behaves same as version 5.6 or previous
  versions, i.e., if browse mode is not available for an app, the focus is
  shown using the thick red rectangle.
* Focus in focus mode, Focus in browse mode, Navigator object: Each of these
  groups contains Color, Thickness, and Style.

    * Color: This edit field allows you to type the HTML color code, i.e.,
      six-character hexadecimal number. For example, "ffffff" is white,
      "ff0000" is red, and so on. Note that "000000" can not be used.
    * Thickness: This edit field allows you to type the thickness of the
      box. You can enter a value between 1 and 30.
    * Style: The choices are Solid, Dash, Dot, Dash dot, and Dash dot-dot.

* Restore defaults: This button allows you to reset your settings to their
  original defaults.

## 6.1에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## 6.0에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## 5.6에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## 5.5에서의 변경사항 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## 5.4에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## 5.3에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## 5.2에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.

## 5.1에서의 변경사항 ##

* Removed debug log output.

## 5.0에서의 변경사항 ##

* Navigator 객체와 포커스 모드의 표시 방식이 바뀌었습니다.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## 4.0에서의 변경사항 ##

* 현재 응용 프로그램이 NVDA가 일시중지인 상태일 경우 포커스 강조 표시가 숨겨지도록 함

## 3.0에서의 변경사항 ##

* Fixed issue regarding expanded combo box.
* 윈도우즈 작업 관리자에서의 문제점 수정.
* 포커스 모드를 표시할 수 있음.

## 2.1에서의 변경사항 ##

* 새 언어 추가 및 번역 업데이트.

## 2.0에서의 변경사항 ##

* 추가 기능 관리자에서 추가 기능에 대한 도움말을 사용할 수 있음.

## 1.1에서의 변경사항 ##

* navigator 객체의 사각형 표시를 점선으로 변경.
* '플러그인 제등록' 버그 수정.

## 1.0에서의 변경사항 ##

* Windows 8에서 Internet Explorer 10 및 Skype navigator 객체의 버그 수정.
* 첫 번째 버전.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
