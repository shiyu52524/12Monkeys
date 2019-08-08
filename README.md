# Scrapy_project
an offline mutiprogessing Scrapy framwork

这个框架是根据我在许多爬虫项目中，所爬取的诸多网站(一些商业网站，较多政府数据库)总结出来的一个架设在localhost的小型爬虫。设计这个框架的初衷是为了将已经学到的爬虫技术设计成一个便于扩展，功能齐全，方便初学者使用的工具；同时也让爬虫开发者减轻开发耗时，达到只需输入网址和匹配规则，就可进行匹配的目的

This small scrapy framework works locally, based on the experience from crawler projects(few Commercial sites,many Government database). that I participated in. The original intention of this is to design a crawling  tool that is easy to expand, full-featured and easy for beginners to use. It also allows the crawler developer to reduce their time for programing - by simply entering the URL and matching rules


# 特点：
* 完全python编写，支持多进程（muliprogress_handler.Dialo方法）
	* 使用的是python内置方法Pool（我承认这个方法存在诸多使用问题与bug）
	* 可通过core变量改变线程数
* 依赖于redis和mongoDB，所以在使用前请在本地开启服务
* 支持断点续爬
* 支持对返回的json文件进行读取处理
* 使用独立的，在redis上运行的IP池进行代理伪装，当然这是一个可以选择的选项
* 为了不让脚本过于枯燥，加入了百分比进度条

# Feature：
* Totally Python ，mutilprogressing is supported（muliprogress_handler.Dialo）
	* mutiprogressing.Pool is used（although there are crashes and bugs caused by the method）
	* you can change progress num by calling muliprogress_handler.core
	* if you have more suggestions about mutiprogressing, pls tell me
* depend on redis & mongoDB, you should start those services before running
* restarting at breakpoint is supported
* a json parser is included
* a separated IP pool  is running on redis for proxy masquerading, which is optional.
* In order not to make the script too boring, a percentage progress bar was added

# TODO
* 数据提取接口（初定使用bs4包）
* 完善IP池工具
* 更加智能的网页解析器
* 结果文件生成接口（CSV,EXCEL）
