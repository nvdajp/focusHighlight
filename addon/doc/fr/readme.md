# Focus Highlight #

* Auteurs : Takuya Nishimoto
* Télécharger [version stable][2]
* Télécharger [version de développement][1]

En dessinant un rectangle coloré, cette extension permet aux utilisateurs
malvoyants, éducateurs voyants ou aux développeurs de suivre l'emplacement
de l'objet navigateur de NVDA et le contrôle de l'objet en focus.

Les couleurs suivantes sont utilisées par cette extension :

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

* Traductions nouvelles et mises à jour.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/14)
  with the latest development versions of NVDA.
* Focus Highlight category of NVDA Settings dialog is now available. Note
  that it works only with NVDA 2018.3 or later.
* [Discussions regarding customizing
  colors](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discussions regarding 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## Changes for 6.0 ##

* Traductions nouvelles et mises à jour.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changements pour la version 5.6 ##

* Traductions nouvelles et mises à jour.
* Résout le problème de compatibilité avec la snapshot de NVDA alpha-16682.

## Changements pour la version 5.5 ##

* Résout le problème avec NVDA 2018.4 et les navigateurs Web Firefox /
  Chrome.

## Changements pour la version 5.4 ##

* Traductions nouvelles et mises à jour.
* Résout  [le problème](https://github.com/nvdajp/focusHighlight/issues/11)
  concernant la compatibilité des versions.

## Changements pour la version 5.3 ##

* Traductions nouvelles et mises à jour.
* Résout  [le problème](https://github.com/nvdajp/focusHighlight/issues/10)
  concernant le navigateur Google Chrome et le mode veille des applications.

## Changements pour la version 5.2 ##

* Traductions nouvelles et mises à jour.

## Changements pour la version 5.1 ##

* Suppression de la sortie du journal en mode débogage.

## Changements pour la version 5.0 ##

* Les indicateurs d'objet navigateur et de mode focus ont été modifiés.
* Plusieurs moniteurs sont pris en charge.
* Il utilise maintenant la technologie GDI Plus pour le dessin.

## Changements pour la version 4.0 ##

* Masquer le rectangle si l'application actuelle est en mode veille.

## Changements pour la version 3.0 ##

* Correction d'un problème concernant la zone de liste déroulante
  développée.
* Correction d'un problème avec le gestionnaire de tâches Windows.
* Capacité d'indiquer le mode focus.

## Changements pour la version 2.1 ##

* Traductions nouvelles et mises à jour.

## Changements pour la version 2.0 ##

* L'aide de l'extension est disponible à partir du Gestionnaire
  d'extensions.

## Changements pour la version 1.1 ##

* Changé objet navigateur de rectangle à traits en escalier.
* Correction d'un problème avec "Recharger les extensions".

## Changements pour la version 1.0 ##

* Dans Internet Explorer 10 et Skype sur Windows 8, correction d'un problème
  avec l'objet navigateur.
* Première version.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
