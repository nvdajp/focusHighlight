# Focus Highlight #

* Authors: Takuya Nishimoto
* Download [stable version][2]
* Download [development version][1]

By drawing a colored rectangle, this addon enables partially sighted users, sighted educators, or developers to track the location of the nvda navigator object and the focused object/control.

The following colors are used by this addon:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e., key types are passed to the control.

To disable object tracking, uninstall the addon.

## Changes for 6.0 ##

* New and updated translations.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13) regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an application, it is always shown that NVDA is in focus mode for the application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to half.

## Changes for 5.6 ##

* New and updated translations.
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* New and updated translations.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11) regarding version compatibility.

## Changes for 5.3 ##

* New and updated translations.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10) regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* New and updated translations.

## Changes for 5.1 ##

* Removed debug log output.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Changes for 4.0 ##

* Hide rectangle if current application is in sleep mode.

## Changes for 3.0 ##

* Fixed issue regarding expanded combo box.
* Fixed issue with Windows Task Manager.
* Ability to indicate the focus mode.

## Changes for 2.1 ##

* New and updated translations.

## Changes for 2.0 ##

* Add-on help is available from the Add-ons Manager.

## Changes for 1.1 ##

* Changed navigator object rectangle to jagged line.
* Fixed issue with 'Reload plugins'.

## Changes for 1.0 ##

* In Internet Explorer 10 and in Skype on Windows 8, fix a problem with the navigator object.
* Initial version.


[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: http://addons.nvda-project.org/files/get.php?file=fh
