# Focus Highlight #

* Auteurs : Takuya Nishimoto
* Télécharger [version stable][2]
* Télécharger [version de développement][1]

En dessinant un rectangle coloré, ce module complémentaire permet aux
utilisateurs malvoyants, éducateurs voyants ou aux développeurs de suivre
l'emplacement de l'objet navigateur de NVDA et l'objet mis en focus ou le
contrôle.

Les couleurs suivantes sont utilisées par ce module complémentaire :

* Rectangle traits mince en ligne pointillé vert, pour indiquer l'objet
  navigateur.
* Rectangle mince rouge, pour indiquer l'objet mis en focus ou le contrôle.
* Rectangle épais rouge, pour indiquer lorsque  l'objet navigateur et
  l'objet mis en focus sont chevauchent.
* Rectangle épais en ligne pointillé bleu, pour indiquer à NVDA qui est en
  mode focus, c'est-à-dire les principaux types sont passés au contrôle.

Pour désactiver le suivi d'objets, désinstallez le module complémentaire.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* Traductions nouvelles et mises à jour.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* Traductions nouvelles et mises à jour.
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* Traductions nouvelles et mises à jour.

## Changes for 5.1 ##

* Removed debug log output.

## Changements pour la version 5.0 ##

* Les indicateurs objet navigateur et le mode focus ont été modifiés.
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
