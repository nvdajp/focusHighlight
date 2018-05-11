# Focus Highlight #

* Auteurs : Takuya Nishimoto
* Télécharger [version stable][2]
* Télécharger [version de développement][1]

En dessinant un rectangle coloré, ce module complémentaire permet aux
utilisateurs malvoyants, éducateurs voyants ou aux développeurs de suivre
l'emplacement de l'objet navigateur de NVDA et l'objet mis en focus ou le
contrôle.

Les couleurs suivantes sont utilisées par ce module complémentaire :

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* Rectangle mince rouge, pour indiquer l'objet mis en focus ou le contrôle.
* Rectangle épais rouge, pour indiquer lorsque  l'objet navigateur et
  l'objet mis en focus sont chevauchent.
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

Pour désactiver le suivi d'objets, désinstallez le module complémentaire.

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Changements pour la version 4.0 ##

* Masquer le rectangle si l'application actuelle est en mode veille.

## Changements pour la version 3.0 ##

* Fixed issue regarding expanded combo box.
* Correction d'un problème avec le gestionnaire de tâches Windows.
* Capacité d'indiquer le mode focus.

## Changements pour la version 2.1 ##

* Traductions nouvelles et mises à jour.

## Changements pour la version 2.0 ##

* L'aide du module complémentaire est disponible à partir du Gestionnaire de
  modules complémentaires.

## Changements pour la version 1.1 ##

* Changé objet navigateur de rectangle à traits en escalier.
* Correction d'un problème avec "Recharger les plugins".

## Changements pour la version 1.0 ##

* Dans Internet Explorer 10 et Skype sur Windows 8, correction d'un problème
  avec l'objet navigateur.
* Première version.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
