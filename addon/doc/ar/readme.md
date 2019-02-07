# Focus Highlight #

* مطورو الإضافة: Takuya Nishimoto
* تحميل [الإصدار النهائي][2]
* تحميل [الإصدار التجريبي][1]

هذه الإضافة تمكن المستخدمين من ضعاف البصر والمعلمين المبصرين والمطورين من
تتبع موضع الكائن المحدد بمؤشر NVDA  أو أي عنصر  أو كائن محدد بمؤشر النظام،
وذلك عن طريق رسم مستطيل ملون. 

تستخدم الإضافة الألوان التالية:

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* مستطيل أحمر رفيع يشير إلى العنصر أو الكائن المحدد بمؤشر النظام
* ومستطيل أحمر عريض للإشارة إلى التداخل بين الكائن الحالي المحدد بمؤشر NVDA
  والكائن أو العنصر المحدد بمؤشر النظام. 
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

لتعطيل تتبع الكائنات يرجى إزالة الإضافة

## Changes for 5.6 ##

* ترجمة الإضافة للغات جديدة وتحديث ترجمتها باللغات الأخرى
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* ترجمة الإضافة للغات جديدة وتحديث ترجمتها باللغات الأخرى
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* ترجمة الإضافة للغات جديدة وتحديث ترجمتها باللغات الأخرى
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* ترجمة الإضافة للغات جديدة وتحديث ترجمتها باللغات الأخرى

## Changes for 5.1 ##

* Removed debug log output.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Changes for 4.0 ##

* Hide rectangle if current application is in sleep mode.

## مستجدات الإصدار 3.0 ##

* Fixed issue regarding expanded combo box.
* إصلاح خطأ كان يحدث عند فتح مدير المهام بويندوز
* إمكانية توضيح نمط الحقول الاستمارية

## مستجدات الإصدار 2.1 ##

* ترجمة الإضافة للغات جديدة وتحديث ترجمتها باللغات الأخرى

## مستجدات الإصدار 2.0 ##

* أصبح من الممكن الوصول لملف المساعدة من مدير الإضافات البرمجية.

## مستجدات الإصدار 1.1 ##

* تغيير شكل مؤشر NVDA من المستطيل إلى خط مسنن
* إصلاح خطأ كان يحدث عند 'إعادة تحميل الملحقات'.

## تعديلات الإصدار 1.0 ##

* تم إصلاح خطأ مرتبط بمؤشر NVDA في كل من Internet Exploer 10 و skype في نظام
  ويندوز 8.
* إصدار أولي


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
