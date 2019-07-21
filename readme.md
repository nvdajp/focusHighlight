# Focus Highlight #

* Authors: Takuya Nishimoto, Karl-Otto Rosenqvist
* Download [stable version][2]
* Download [development version][1]

By drawing a colored rectangle, this addon enables partially sighted users, sighted educators, or developers to track the location of the nvda navigator object and the focused object/control.

The following colors are used by this addon:

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e., key types are passed to the control.

To toggle object tracking, press NVDA+Alt+P. You can assign other gestures using the Input Gestures dialog.
Note that it works with NVDA 2018.3 or later.
Otherwise, you should disable or uninstall the addon itself for disabling object tracking.

When Focus Highlight category of NVDA Settings dialog is available, following items can be used.

* Make focus mode the default: This checkbox is enabled by default. When it is unchecked, this add-on behaves same as version 5.6 or previous versions, i.e., if browse mode is not available for an app, the focus is shown using the thick red rectangle.
* Focus in focus mode, Focus in browse mode, Navigator object: Each of these groups contains Color, Thickness, and Style.
  * Color: This edit field allows you to type the HTML color code, i.e., six-character hexadecimal number. For example, "ffffff" is white, "ff0000" is red, and so on. Note that "000000" can not be used.
  * Thickness: This edit field allows you to type the thickness of the box. You can enter a value between 1 and 30.
  * Style: The choices are Solid, Dash, Dot, Dash dot, and Dash dot-dot.
* Restore defaults: This button allows you to reset your settings to their original defaults.

## Changes for 6.3 ##

* New and updated translations.
* Fixed the issue that dash styles of focus (in browse mode) and navigator object are not able to change.
* Fixed the issue that 'Cancel' button of setting panel does not work after 'Restore defaults' button is pressed.

## Changes for 6.2 ##

* New and updated translations.
* You can now turn object tracking on and off using NVDA+Alt+P. Karl-Otto Rosenqvist contributed for this.

## Changes for 6.1 ##

* New and updated translations.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14) with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the default'](https://github.com/nvdajp/focusHighlight/issues/13)

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
