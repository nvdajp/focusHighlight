# Focus Highlight #

* 저자: Takuya Nishimoto
* Download [안정 버전][2]
* Download [개발 버전][1]

이 추가 기능은 NVDA navigator 객체와 초점이 있는 객체/컨트롤의 위치를 색깔 있는 사각형으로 강조 표시합니다. 시각 장애인
사용자, 시각 장애인 교육자, 또는 개발자에게 유용합니다.

다음의 2 색이 이 추가 기능에 의해 사용됩니다:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* 빨간색 얇은 선, 초점이 있는 객체/콘트롤을 나타냅니다.
*  navigator 객체와 포커스가 있는 객체가 겹치는 경우, 빨간색 굵은 선이 표시됩니다.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

개체의 하이라이트를 비활성화하려면 이 추가 기능을 제거합니다.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
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

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
