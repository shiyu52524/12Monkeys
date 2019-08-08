# Scrapy_project
an offline mutiprogessing Scrapy framwork

这个框架是根据我在许多爬虫项目中，所爬取的诸多网站(一些商业网站，较多政府数据库)总结出来的一个架设在localhost的小型爬虫
This small scrapy framework works locally, based on the experience from some crawler projects(few Commercial sites,many Government database).


# 特点：
* 完全python编写，支持多进程（muliprogress_handler.Dialo方法）
	* 使用的是python内置方法Pool（我承认这个方法存在诸多使用问题与bug）
	* 可通过core变量改变线程数
* 依赖于redis和mongoDB，所以在使用前请在本地开启服务
* 支持断点续爬
* 为了不让脚本过于枯燥，加入了百分比进度条

# Feature：
* Totally Python ，mutilprogressing is supported（muliprogress_handler.Dialo）
	* mutiprogressing.Pool is used（although there are crashes and bugs caused by the method）
	* you can change progress num by calling muliprogress_handler.core
	* if you have more suggestions about mutiprogressing, pls tell me
* depend on redis & mongoDB, you should start those services before running
* restarting at breakpoint is supported
* In order not to make the script too boring, a percentage progress bar was added
