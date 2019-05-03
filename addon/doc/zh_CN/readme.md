# 焦点突出显示 Focus Highlight #

* 作者: Takuya Nishimoto
* 下载 [稳定版][2]
* 下载 [开发板][1]

通过绘制一个彩色的矩形，这个插件可以让弱视用户，有视力的教育工作者或开发者跟踪nvda导航器对象的位置和焦点对象/控件。

此插件使用以下颜色：

* 绿色的锯齿线，以指示导航对象。
* 红色的细长矩形，以指示聚焦的对象/控件。
* 红色厚矩形，用于指示导航器对象和聚焦对象何时重叠。
* 蓝色的粗斜长方形，表示NVDA处于对焦模式，即按键类型传递给控件。

要禁用对象跟踪，请卸载插件。

## 版本5.6 ##

* 更新新的翻译。
* 解决NVDA预览版alpha-16682的兼容性问题。

## 版本 5.5 ##

* 解决NVDA 2018.4和Firefox / Chrome网络浏览器的问题。

## 版本 5.4 ##

* 更新新的翻译。
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/11)
  regarding version compatibility.

## 版本 5.3 ##

* 更新新的翻译。
* Addresses [the issue](https://github.com/nvdajp/focusHighlight/issues/10)
  regarding Chrome browser and application sleep mode.

## 版本 5.2 ##

* 更新新的翻译。

## 版本 5.1 ##

* 删除调试日志输出。

## 版本 5.0 ##

* 导航器对象和聚焦模式的指示符已更改。
* 支持多个监视器。
* 现在使用GDI Plus技术进行绘图。

## 版本 4.0 ##

* 如果当前应用程序处于睡眠模式，则隐藏矩形。

## 版本 3.0 ##

* 修复了有关插件组合框的问题。
* 修复了Windows任务管理器的问题。
* 支持指示对焦模式。

## 版本 2.1 ##

* 更新新的翻译。

## 版本 2.0 ##

* 插件管理器现在可以查看插件帮助。

## 版本 1.1 ##

* 将导航器对象矩形更改为绿色锯齿线。
* 修复了'重新加载插件'的问题。

## 版本 1.0 ##

* 在Internet Explorer 10和Windows 8上的Skype中，修复了导航器对象的问题。
* 发布初始版本。


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=fh-dev

[2]: https://addons.nvda-project.org/files/get.php?file=fh
