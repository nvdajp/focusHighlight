# Focus Highlight #

* Autores: Takuya Nishimoto
* Descargar [versión estable][2]
* Descarga [versión de desenvolvemento][1]

Ó dibuxar un rectángulo coloreado, este complemento permite ós usuarios con
deficencia visual, educadores videntes, ou desenvolvedores seguir a posición
do navegador de obxectos do NVDA e o obxecto ou control enfocado.

As seguintes cores utilízanse por este complemento:

* Rectángulo fino verde de liñas punteadas para indicar o navegador de
  obxectos.
* Rectángulo fino bermello amosa que NVDA está en modo exploración, e que
  éste é o obxecto/control enfocado.
* Rectángulo groso bermello amosa que NVDA está en modo exploración, e que
  éste é o obxecto/control enfocado.
* Rectángulo groso azul de liñas punteadas indica que NVDA está en modo
  foco, p.ex., as pulsacións de teclas pásanse ao control.

Para deshabilitar o seguemento de obxectos, deshabilita ou desinstala o
complemento.

Cando a categoría Focus Highlight do diálogo de Opcións de NVDA está
dispoñible, pódense utilizar os seguintes elementos.

* Predeterminar modo foco: Esta caixa de verificación está habilitada por
  defecto. Cando se desmarca, este complemento compórtase da mesma maneira
  que na versión 5.6 ou anteriores, p.ex. se o modo exploración non está
  dispoñible nunha app, o foco amósase utilizando o rectángulo vermello
  groso.
* Foco en modo foco, Foco en modo exploración, Obxecto no navegador: Cada un
  destes grupos contén Cor, Grosor e Estilo.

    * Cor: Esta caixa de edición permíteche escribir o código de cor HTML,
      p.ex. número hexadecimal de seis caracteres. Por exemplo, "ffffff" é
      branco, "ff0000" é vermello, e así. Ten en conta que "000000" non se
      pode utilizar.
    * Grosor: Esta caixa de edición permíteche escribir o grosor da
      caixa. Podes introducir un valor entre 1 e 30.
    * Estilo: As alternativas son Solid (Sólido), Dash (Guión), Dot (Punto),
      Dash dot (Guión punto) e Dash dot-dot (Guión punto-punto).

* Restaurar por defecto: Este botón permíteche restablecer os teus axustes
  aos seus orixinais por defecto.

## Cambios para 6.1 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/14)
  coas últimas versións de desenvolvemento do NVDA.
* A categoría do diálogo de Opcións de NVDA Focus Highlight xa está
  dispoñible. Ten en conta que só funciona con NVDA 2018.3 ou posterior.
* [Discusións sobre a persoalización de
  cores](https://github.com/nvdajp/focusHighlight/issues/3)
* [Discusións sobre 'Make focus mode the
  default'](https://github.com/nvdajp/focusHighlight/issues/13)

## Cambios para 6.0 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/13)
  en relación co modo exploración.
* Dende esta versión, se o modo exploración do NVDA non está dispoñible para
  unha aplicación, amósase sempre que NVDA está en modo foco para a
  aplicación, en lugar de utilizar o rectángulo groso vermello.
* O grosor da liña que representa o modo foco reduciuse á metade.

## Cambios para 5.6 ##

* Traduccións novas e actualizadas.
* Arranxa o problema de compatibilidade coa compilación de desenvolvemento
  de NVDA alpha-16682.

## Cambios para 5.5 ##

* Soluciona o problema con NVDA 2018.4 e os navegadores web Firefox/Chrome.

## Cambios para 5.4 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/11)
  referente ás versións compatibles.

## Cambios para 5.3 ##

* Traduccións novas e actualizadas.
* Soluciona [o problema](https://github.com/nvdajp/focusHighlight/issues/10)
  en relación co navegador Chrome e o modo de aplicación durminte.

## Cambios para 5.2 ##

* Traduccións novas e actualizadas.

## Cambios para 5.1 ##

* Eliminada a saída ó rexistro de depuración.

## Cambios para 5.0 ##

* Cambiáronse os indicadores para o navegador de obxectos e para o Modo
  Foco.
* Admítense múltiples monitores.
* Agora usa a tecnoloxía GDI Plus para dibuxar.

## Cambios para 4.0 ##

* Agocha o rectángulo se a aplicación actual está en modo durminte.

## Cambios para 3.0 ##

* Arranxado un problema vencellado coa Caixa combinada expandida.
* Correxido un problema co xestor de tarefas de Windows.
* Capacidade para indicar modo foco.

## Cambios para 2.1 ##

* Traduccións novas e actualizadas.

## Cambios para 2.0 ##

* A axuda do complemento está dispoñible no Administrador de Complementos.

## Cambios para 1.1 ##

* Cambiado o rectángulo do navegador de obxectos por unha liña irregular.
* Correxido un problema con 'Recargar plugins'.

## Cambios para  1.0 ##

* No Internet Explorer 10 e no Skype en Windows 8, arránxase un problema co
  navegador de obxectos.
* Versión inicial.


[[!tag dev stable]]

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
