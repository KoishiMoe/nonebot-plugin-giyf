<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot-plugin-giyf

_适用于 [NoneBot2](https://v2.nonebot.dev) 的搜索引擎插件_

</div>

------

![Python](https://img.shields.io/badge/python-3.8%2B-lightgrey)
![nonebot2](https://img.shields.io/badge/nonebot2-2.0.0b2-yellowgreen)
[![GitHub license](https://img.shields.io/github/license/KoishiStudio/nonebot-plugin-giyf)](https://github.com/KoishiStudio/nonebot-plugin-giyf/blob/main/LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-giyf?color=blue)](https://pypi.org/project/nonebot-plugin-giyf/)

[![GitHub issues](https://img.shields.io/github/issues/KoishiStudio/nonebot-plugin-giyf)](https://github.com/KoishiStudio/nonebot-plugin-giyf/issues)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/KoishiStudio/nonebot-plugin-giyf?include_prereleases)](https://github.com/KoishiStudio/nonebot-plugin-giyf/releases)
[![GitHub all releases downloads](https://img.shields.io/github/downloads/KoishiStudio/nonebot-plugin-giyf/total)](https://github.com/KoishiStudio/nonebot-plugin-giyf/releases)
![GitHub contributors](https://img.shields.io/github/contributors/KoishiStudio/nonebot-plugin-giyf)
![GitHub Repo stars](https://img.shields.io/github/stars/KoishiStudio/nonebot-plugin-giyf?style=social)

------

本项目是 [Flandre](https://github.com/KoishiStudio/Flandre) 的
[quick_search](https://github.com/KoishiStudio/Flandre/tree/main/src/plugins/quick_search) 组件，经简单修改成为独立插件发布。

同时，本插件和 [nonebot-plugin-mediawiki](https://github.com/KoishiStudio/nonebot-plugin-mediawiki) 有着类似的结构，至于原因嘛……(ಡωಡ)

## 用途

如题，`Google is your friend`，用于指引群友快速 访 ~~(tui)~~ 问 ~~(dao)~~ 谷歌娘（在中国大陆大概就是度娘了～）

## 使用说明
```plaintext
Tip：本插件的设置系统和 nonebot plugin-mediawiki 基本一致，因此如果你使用过前者，那么本插件的配置应该很容易上手
```
### TL;DR

查询： `？前缀 关键词`

添加（全局）搜索引擎： `search.add` `search.add.global`

快速添加： `search.add(.global) [预置的搜索引擎名称] [自定义前缀（可选）]`

删除（全局）搜索引擎： `search.delete` `search.delete.global`

修改（全局）搜索引擎： `search.default` `search.default.global`

查看搜索引擎列表： `search.list` `search.list.global`

**其中所有非全局指令均需要在目标群中进行，所有全局指令均只有Bot管理员能执行**

### 参数说明：

#### 快速添加
* 预置的搜索引擎名称：bot内置的引擎名称，目前有 `google` `bing` `baidu` `duckduckgo` `startpage` `zhwikipedia` `enwikipedia` `yahoo` `yandex`
* 自定义前缀：你可以使用自己的前缀来代替bot预设的前缀；关于“前缀”的说明见下

#### 前缀
就是你给这个搜索引擎起的代号，好记就行，例如给谷歌娘叫`go`，给度娘叫`bd`，等等。**只支持英文和数字**

#### 链接：
需要使用搜索引擎的搜索url，**而非首页url**；这类url的明显特征就是，其中带有`%s`，并且在搜索时`%s`会被替换成你的搜索关键字

例如：
```plaintext
Google: https://www.google.com/search?q=%s
Baidu: https://www.baidu.com/s?wd=%s
Bing: https://www.bing.com/search?q=%s
Duckduckgo: https://duckduckgo.com/?q=%s
```

获取这类链接有三种方法：

1. ~~问谷歌~~

（经过查找，只找到了谷歌和百度的……）


2. 查看浏览器设置

打开浏览器的搜索引擎设置，这里会出现默认配置好的搜索引擎，以及一些你访问过的搜索引擎。点击“编辑”，在“查询URL”一栏通常就是我们要找的

```plaintext
Tip：部分搜索引擎在此可能显示的有一些变量，例如 {google:baseURL}search?q=%s ，本插件无法识别这种，还请留意
```

3. ~~人工智能（不是~~

打开你要使用的搜索引擎，随便搜点什么（建议使用英文或数字，中文被编码后根本分不清……），把链接复制下来，把你原先输入的搜索关键字换成`%s`，大功告成！

```plaintext
Tip：某些搜索引擎的链接可能包含你的一些个人信息，建议在隐私浏览窗口中进行上述操作。
另外，通常情况下，搜索关键词后面的附加参数并不会影响搜索结果，因此一般可以去除
例如： https://www.bing.com/search?q=%s&form=xxxx 其中的 &from=xxxx就可以去掉 
```

## TODO
- [x] 内置一些常用的搜索引擎，用来快速添加