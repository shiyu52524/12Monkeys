# 12Monkeys
an async crawler framework

![](https://img.shields.io/badge/Build-Master-brightgreen) 
![](https://img.shields.io/badge/Vision-v0.0.1-blue)
![](https://img.shields.io/badge/Python-3.7-orange)
![](https://img.shields.io/badge/Author-shiyu52524-lightgrey)


这个框架是根据我在许多爬虫项目中，所爬取的诸多网站(一些商业网站，较多政府数据库)总结出来的一个架设在localhost的小型爬虫。设计这个框架的初衷是为了让爬虫开发者减轻开发耗时，达到只需输入网址(CSV/Excel文件)和匹配规则，就可进行匹配的目的

This framework is based on the experience of some spider projects(some Commercial sites and Government database) I participated in. The intention of this is to design a tool that allows developers to write less, crawling more - by simply entering URLs(or CSV/Excel files) and matching rules


# 特点：

* 完全python编写，封装好的异步多进程方法（muliprogress_handler.Dialo方法）
 * 使用python内置多线程方法Pool（我承认这个方法存在诸多使用问题与bug）
 * 可通过muliprogress_handler.core变量改变进程数
 * 使用redis进行进程通信
* 网页解析和网页下载是分开的，爬虫会在后台将所有爬取任务的response或者json文件储存在DB下
* 依赖于redis和mongoDB，所以在使用前请在本地开启服务
* 支持断点续爬
* 支持对json文件进行处理
* （可选）使用独立的，在redis上运行的IP池进行代理伪装
* 为了不让脚本过于枯燥，加入了百分比进度条

# Feature：
* Totally writen in Python, mutilprogressing is supported（muliprogress_handler.Dialo）
 * mutiprogressing.Pool is used（although there are crashes and bugs caused by the method）
 * Able to change progress num by calling muliprogress_handler.core
 * any suggestions about mutiprogressing, pls tell me
* page parsing and downloading are separated
* depending on redis & mongoDB, start those services before running
* restarting at breakpoint is supported
* a json parser is included
* (Optional)a separated IP pool is running on redis
* In order not to make the script too boring, a percentage progress bar was added

# TODO
* 数据提取接口（初定使用bs4包）
* 完善IP池工具
* 更加智能的网页解析器
* 结果文件生成接口（CSV,EXCEL）

PS 最近在做别的项目，这个暂时放一放
