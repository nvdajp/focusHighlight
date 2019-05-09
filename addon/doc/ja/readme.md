# Focus Highlight #

* 作者: Takuya Nishimoto
* ダウンロード [安定版][2]
* ダウンロード [開発版][1]

このアドオンは、NVDA
のナビゲーターオブジェクトや、フォーカスのあるオブジェクト・コントロールの場所を、色のついた長方形で強調して表示します。画面の見えにくい人、晴眼の指導者、開発者にとって有用です。

以下の色を使っています：

* Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and
  this is the navigator object.
* Red thin rectangle shows NVDA is in browse mode, and this is the focused
  object/control.
* Red thick rectangle shows NVDA is in browse mode, and this is both the
  navigator object and the focused object which are overlapping.
* Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e.,
  key types are passed to the control.

オブジェクトのハイライトを無効にするには、このアドオンをアンインストールしてください。

## Changes for 6.0 ##

* 新規の翻訳と翻訳の更新。
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/13)
  regarding the browse mode.
* Since this version, if the browse mode of NVDA is not available for an
  application, it is always shown that NVDA is in focus mode for the
  application, rather than using the red thick rectangle.
* The thickness of the line representing the focus mode has been reduced to
  half.

## Changes for 5.6 ##

* 新規の翻訳と翻訳の更新。
* Addresses the compatibility issue with NVDA snapshot alpha-16682.

## Changes for 5.5 ##

* Addresses the issue with NVDA 2018.4 and Firefox/Chrome web browsers.

## Changes for 5.4 ##

* 新規の翻訳と翻訳の更新。
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## Changes for 5.3 ##

* 新規の翻訳と翻訳の更新。
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## Changes for 5.2 ##

* 新規の翻訳と翻訳の更新。

## Changes for 5.1 ##

* Removed debug log output.

## 5.0 での変更点 ##

* ナビゲーターオブジェクトとフォーカスモードの表示が変わりました。
* 複数モニタをサポートしました。
* 描画にはGDI Plus技術を使用するようになりました。

## 4.0 での変更点 ##

* アプリケーションがスリープモードにある時に四角を隠すようにしました。

## 3.0 での変更点 ##

* 拡張コンボボックスでの不具合を修正。
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
