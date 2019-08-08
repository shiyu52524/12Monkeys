# MonkeyKing
an async crawler framwork

美猴王一根毛发就能变化成一只猴子，异步分布式多进程爬虫就跟它们一样，能够在互联网深处挖掘到我们想要的信息，避免了枯燥的人工操作

这个框架是根据我在许多爬虫项目中，所爬取的诸多网站(一些商业网站，较多政府数据库)总结出来的一个架设在localhost的小型爬虫。设计这个框架的初衷是为了将已经学到的爬虫技术设计成一个便于扩展，功能齐全，方便初学者使用的工具；同时也让爬虫开发者减轻开发耗时，达到只需输入网址(CSV/Excel文件)和匹配规则，就可进行匹配的目的

This framework is based on the experience from spider projects(some Commercial sitesand Government database) I participated in. The intention of this is to design a tool that allows developers to write less, crawling more - by simply entering URLs(or CSV/Excel files) and matching rules


# 特点：

* 完全python编写，支持异步多进程（muliprogress_handler.Dialo方法）
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
