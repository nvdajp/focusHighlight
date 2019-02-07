# Focus Highlight #

* Авторы: Takuya Nishimoto
* Загрузить [стабильную версию][2]
* Загрузить [разрабатываемую версию][1]

Рисуя цветной прямоугольник, это дополнение позволяет слабовидящим
пользователям, зрячим педагогам, или разработчикам отслеживать
местоположение объекта навигатора NVDA и объект/тип управление в фокусе.

В этом дополнении используются следующие цвета:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* Красный тонкий прямоугольник указывает объект/тип управления в фокусе.
* Красный толстый прямоугольник для указания наложения объекта навигатора и
  объекта в фокусе.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

Чтобы отключить отслеживание объекта, удалите дополнение.

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

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
