# Focus Highlight #

* Autores: Takuya Nishimoto
* Descargar [versión estable][2]
* Descarga [versión de desarrollo][1]

Al dibujar un rectángulo coloreado, este complemento capacita a los usuarios
con deficiencia visual, educadores videntes, o desarrolladores para seguir
la posición del navegador de objetos de NVDA y del objeto o control
enfocado.

Los siguientes colores se utilizan con este complemento:

* Un rectángulo verde de líneas punteadas indica que NVDA está en modo
  exploración, y muestra el navegador de objetos.
* Un rectángulo rojo delgado indica que NVDA está en modo exploración, y
  muestra el objeto o control enfocado.
* Un rectángulo rojo grueso indica que NVDA está en el modo exploración, y
  se muestra cuando el navegador de objetos y el objeto enfocado se
  superponen.
* Un rectángulo de líneas punteadas gruesas azules indica que NVDA está en
  modo foco, es decir, las teclas se pasan al control.

Para deshabilitar el seguimiento de objetos, desactiva o desinstala el
complemento.

Cuando se encuentre disponible la categoría Focus Highlight del diálogo de
opciones de NVDA, podrán usarse los siguientes elementos.

* Establecer el modo foco por defecto: esta casilla de verificación se
  encuentra marcada por defecto. Si está desmarcada, el complemento se
  comportará igual que en la versión 5.6 o anteriores, es decir: si el modo
  exploración no está disponible en una aplicación, el foco se representa
  con un rectángulo rojo y grueso.
* Foco en modo foco, foco en modo exploración, navegador de objetos: cada
  uno de estos grupos contiene color, grosor y estilo.

    * Color: este cuadro de edición te permite escribir el código del color
      HTML, es decir, un número de seis caracteres hexadecimales. Por
      ejemplo, "ffffff" es blanco, "ff0000" es rojo, y así
      sucesivamente. Ten en cuenta que "000000" no se puede usar.
    * Grosor: este cuadro de edición permite escribir el grosor del
      recuadro. Puedes introducir un valor entre 1 y 30.
    * Estilo: las opciones son sólido, guión, punto, guión punto, y guión
      punto punto.

* Restaurar por defecto: este botón te permite restablecer los ajustes a sus
  valores originales.

## Cambios para 6.1 ##

* Traducciones nuevas y actualizadas.
* Soluciona [la
  incidencia](https://github.com/nvdajp/focusHighlight/issues/14) con las
  versiones de desarrollo de NVDA más recientes.
* La categoría Focus Highlight ya se encuentra disponible en el diálogo de
  opciones de NVDA. Ten en cuenta que sólo funciona con NVDA 2018.3 o
  posterior.
* [Debates sobre la personalización de
  colores](https://github.com/nvdajp/focusHighlight/issues/3)
* [Debates sobre 'Establecer el modo foco por
  defecto'](https://github.com/nvdajp/focusHighlight/issues/13)

## Cambios para 6.0 ##

* Traducciones nuevas y actualizadas.
* Resuelve [la
  incidencia](https://github.com/nvdajp/focusHighlight/issues/13)
  relacionada con el modo exploración.
* A partir de esta versión, si el modo exploración de NVDA no está
  disponible en alguna aplicación, siempre se indica que está activo el modo
  foco en esa aplicación en vez de usar el rectángulo rojo grueso.
* El grosor de la línea que representa el modo foco se ha reducido a la
  mitad.

## Cambios para 5.6 ##

* Traducciones nuevas y actualizadas.
* Soluciona problemas de compatibilidad con la snapshot de NVDA alpha-16682.

## Cambios para 5.5 ##

* Resuelve la incidencia con NVDA 2018.4 y los navegadores web Firefox y
  Chrome.

## Cambios para 5.4 ##

* Traducciones nuevas y actualizadas.
* Soluciona [la
  incidencia](https://github.com/nvdajp/focusHighlight/issues/11)
  relacionada con la compatibilidad de versiones.

## Cambios para 5.3 ##

* Traducciones nuevas y actualizadas.
* Resuelve [la
  incidencia](https://github.com/nvdajp/focusHighlight/issues/10)
  relacionada con el navegador Chrome y el modo silencioso en aplicaciones.

## Cambios para 5.2 ##

* Traducciones nuevas y actualizadas.

## Cambios para 5.1 ##

* Se ha eliminado la salida del registro de depuración.

## Cambios para 5.0 ##

* Se cambiaron los indicadores para navegador de objetos y Modo Foco.
* Se admiten múltiples monitores.
* Ahora utiliza la tecnología GDI Plus para dibujar.

## Cambios para 4.0 ##

* Oculta el rectángulo si la aplicación actual está en modo durmiente.

## Cambios para 3.0 ##

* Corregido un problema relacionado con el cuadro combinado expandido.
* Corregido un problema  con el gestor de tareas de Windows.
* Capacidad para indicar el modo foco.

## Cambios para 2.1 ##

* Traducciones nuevas y actualizadas.

## Cambios para 2.0 ##

* La ayuda del complemento está disponible en el Administrador de
  Complementos.

## Cambios para 1.1 ##

* Se cambió el rectángulo del navegador de objetos por  una línea quebrada.
* Corregido un problema  con 'Recargar plugins'.

## Cambios para 1.0 ##

* En Internet Explorer 10 y en Skype en Windows 8,se soluciona un problema
  con el navegador de objetos.
* Versión inicial.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
