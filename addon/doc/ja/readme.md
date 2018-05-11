# Focus Highlight #

* 作者: Takuya Nishimoto
* ダウンロード [安定版][2]
* ダウンロード [開発版][1]

このアドオンは、NVDA
のナビゲーターオブジェクトや、フォーカスのあるオブジェクト・コントロールの場所を、色のついた長方形で強調して表示します。画面の見えにくい人、晴眼の指導者、開発者にとって有用です。

以下の色を使っています：

* Green thin dashed dotted line rectangle, to indicate the navigator object.
* 赤色の細い線：フォーカスのあるオブジェクト・コントロールを示します。
* 赤色の太い線：ナビゲーターオブジェクトとフォーカスが重なっていることを示します。
* Blue thick dotted line rectangle, to indicate NVDA is in focus mode,
  i.e. key types are passed to the control.

オブジェクトのハイライトを無効にするには、このアドオンをアンインストールしてください。

## Changes for 5.0 ##

* Indicators of navigator object and focus mode were changed.
* Multiple monitors are supported.
* It now uses GDI Plus technology for drawing.

## Changes for 4.0 ##

* Hide rectangle if current application is in sleep mode.

## 3.0 での変更点 ##

* Fixed issue regarding expanded combo box.
* Windows Task Managerでの不具合を修正。
* フォーカスモードを表示する機能。

## 2.1 での変更点 ##

* 新規の翻訳と翻訳の更新。

## 2.0 での変更点 ##

* アドオンマネージャーからアドオンの説明を利用できます。

## 1.1 での変更点 ##

* ナビゲーターオブジェクトの表示を緑のギザギザの線に変更しました。
* プラグインの再読み込みの不具合修正。

## 1.0 での変更点 ##

* Windows 8 における Internet Explorer 10 と Skype のナビゲーターオブジェクトの不具合の修正
* 最初のバージョンです。


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
