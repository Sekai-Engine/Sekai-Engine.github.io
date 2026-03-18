<!-- markdown.html -->

# WebGal引擎测评

[返回目录](../目录.md)

WebGal Engine 是由TypeScript编写的作为专为现代浏览器环境设计的视觉小说（Visual Novel, VN）开源引擎，凭借其轻量的架构与优秀的美术风格正成为独立游戏开发者的新宠。

## 开源协议与授权

webgal采用 Mozilla Public License 2.0 (MPL 2.0) 协议，介于宽松协议（如 MIT、Apache）和强 copyleft 协议（如 GPL）之间，主要体现为文件级的开源传染政策：如果改了哪个文件，文件就必须开源；但这个文件和私有代码放在一起打包，私有代码不需要一同开源。

对于独立游戏开发者和小型工作室而言，可以算比较宽松且安全的协议政策。

## 下载

可以通过[官网](https://www.openwebgal.com)直接下载，或者在[github](https://github.com/OpenWebGAL/WebGAL_Terre/releases)下载。

webgal提供了安卓端、windows端与linux端三类主流平台的安装包。

## 开发演示

### 编辑器

编辑器是直接以web服务的形式提供，可以实现远程部署，但是游戏数据将存储在编辑器环境中，没有发现数据导出的功能：

![](/static/img/webgal/webgal_1.png)

### 开发语言

开发使用的语言与[slang](https://github.com/Sekai-Engine/slang)较为相似，以下是一个简单例子：

```
WebGAL:你好
; 分号后的内容会被视作注释，不运行
changeBg:testBG03.jpg -next; // -next会立刻执行下一条语句
WebGAL:添加testBG03背景并输出当前内容 -notend;
changeFigure:stand.webp -next;
choose:选项1:Chapter-2.txt|选项2;
WebGAL:选项2继续演出...... -notend;
```

相较于[slang](https://github.com/Sekai-Engine/slang)语言，webgal的脚本语言在设置演出的过程中主要依赖类似注入变量的形式，关键词容易更多，为缓解编写困难的问题，webgal编辑器提供了可视化功能，可以通过按钮直接编辑：

![](/static/img/webgal/webgal_2.png)

### 导出功能

测试4.5.17 (2025-12-05)版本显示，导出功能支持平台主要为web，其次支持客户端与安卓端，使用electron进行打包，但是linux好像支持得不是很好，archlinux编译出来以后好像没跑起来，打包出来的程序也不是单个可执行文件，可以考虑学习学习sekai引擎的[sekai-pack](https://github.com/Sekai-Engine/sekai-pack)(笑)

![](/static/img/webgal/webgal_3.png)

程序也没找到交叉编译功能：即跨系统编译，比如linux系统编译到windows，按道理来说使用electron架构的话应该在这方面会很擅长。


## 总结

webgal的特性比较明显：对于组织性协同开发团队而言，WebGal 以 Web 服务形式提供的编辑器是一大优势，支持远程部署，团队成员可以通过搭建云环境提升了协作效率；对于大型开发团队，特别是不满足于只做文字冒险游戏的团队需要关注引擎的上限问题，webgal未提供通用引擎的开发能力，特别是3D仿真等复杂交互；对于独立开发者而言，WebGal 引擎是快速搭建游戏demo的瑞士军刀。



### 打分环节

| 评价类型 |        星级        |  评分值  |
| :----------: | :-------------: | :---------: |
|     总分      | ★★★★☆ | （4/5） |
|   易用性    | ★★★★★ | （5/5） |
| 平台兼容 | ★★★☆☆ | （3/5） |

