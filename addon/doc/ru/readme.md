# Focus Highlight #

* Авторы: Takuya Nishimoto
* Загрузить [стабильную версию][2]
* Загрузить [разрабатываемую версию][1]

Рисуя цветной прямоугольник, это дополнение позволяет слабовидящим
пользователям, зрячим педагогам, или разработчикам отслеживать
местоположение объекта навигатора NVDA и объект/тип управление в фокусе.

В этом дополнении используются следующие цвета:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

To disable object tracking, disable or uninstall the addon.

When Focus Highlight category of NVDA Settings dialog is available,
following items can be used.

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

## Changes for 6.1 ##

* Новые и обновлённые переводы.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## Changes for 6.0 ##

* Новые и обновлённые переводы.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changes for 5.6 ##

* Новые и обновлённые переводы.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Новые и обновлённые переводы.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Новые и обновлённые переводы.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Новые и обновлённые переводы.

## Changes for 5.1 ##

* Removed debug log output.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Изменения для 4.0 ##

* Скрыт прямоугольник, если текущее приложение находится в режиме сна.

## Изменения для 3.0 ##

* Fixed issue regarding expanded combo box.
* Исправлена проблема с диспетчером задач Windows.
* Возможность указать режим фокуса.

## Изменения для 2.1 ##

* Новые и обновлённые переводы.

## Изменения для 2.0 ##

* Справка дополнения доступна в диспетчере дополнений.

## Изменения для 1.1 ##

* Изменён прямоугольник объекта навигатора пунктирной линией.
* Исправлена проблема с 'Обновить модули'.

## Изменения для 1.0 ##

* В Internet Explorer 10 и в Skype в Windows 8, решена проблема с объектом
  навигатора.
* Начальная версия.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
