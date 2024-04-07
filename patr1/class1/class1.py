# -*- coding: utf-8 -*-
# @file: class1.py
# @time: 2024 
# @user: Nemo

"""
环境介绍

virtualenv
virtualenvwrapper-win
pipenv

"""
"""
virtualenv的安装和应用
(windows)安装步骤:
1、pip安装virtualenv
2、pip安装虚拟环境管理包virtualenvwrapper-win
3、创建一个存放虚拟环境的目录(建议命名为.env或者.virtualenv)
4、配置环境变量(变量名:WORKON HOME,值:上面创建的目录路径)


virtualenv的使用命令
虚拟环境的一些命令:
workon
列出所有的虚拟环境
进入指定的虚拟环境
退出当前的虚拟环境
创建虚拟环境
删除虚拟环境
workon [name]
deactivate
mkvirtualenv [name]
rmvirtualenv [name]
包安装:
虚拟环境中安装对应的依赖包进入虚拟环境直接使用pipinstall 进行安装


"""
"""
pipenv 集成了 pip 和 virtualenv 两者的功能

安装 pip install pipenv
创建虚拟环境
    1，创建文件夹 mkdir py3env
    2，进入文件夹 cd py3env
    3，初始化虚拟环境 pipenv install
        创建好虚拟环境之后会生成:一个Pipfile文件和一个Pipfile.lock
    项目提交时,可将'Pipfile'文件和'Pipfile.lock'文件一并提交,待其其他开发克隆下载,
    根据此Pipfile运行命令pipenvinstall--dev生成自己的虚拟环境1.
    Pipfile.lock文件是通过hash算法将包的名称和版本,及依赖关系生成哈希值,可以
    保证包的完整性。


"""
""" 
结构介绍
1、readme:对项目的整体介绍,同时也是一份使用手册,需要时常维护更新。通常为README.rst/README.md
2、LICENSE:阐述该项目的许可说明和授权
3、setup.py:通过setup把核心代码打包发布
4、sample:存放项目的核心代码。
5、requirements.txt:存放该项目所有依赖的第三方库
6、docs:包的参考文档
7、tests:所有的代码测试都归存放于该目录下
8、makefile用于项目的命令管理(开源项目广泛使用)
根据项目需求添加其他的文件和目录


"""
"""
工程结构化
在实践层面,
"结构化"意味着通过编写简洁的代码,并且正如文件系统中文文件和目录的组织一样,代码应该使
逻辑和依赖清晰,在一个健康的开发周期中,代码风格,APli设计和自动化是非常关键的。同样的,对于工程的架
构,仓库的结构也是关键的一部分。
当一个潜在的用户和贡献者登录到您的仓库页面时,他们会看到这些:
工程的名字
工程的描述
一系列的文件
这是Kenneth Reitz(python语言总架构师)推荐的标准仓库样式:https://github.com/kennethreitz/samplemod


"""
"""
pipenv管理模块和包
在虚拟环境中安装模块或者包pipenvinstall包名(注意点在当前项目路径下执行以上命令)
通过-dev指明只安装在开发环境中(开发环境是你当前开发的环境,生产环境早上线部署的实际环境)
pipenv install dev requests
安装包记录是在[dev-packages]部分,或是[packages]部分。
在安装时,指定-dev参数,则只安装[dev-packages]下的包;若安装时不定指定-dev参数,只会安装[packages]包下面的模块。
卸载虚拟环境的模块包pipenvuninstall包名
查看安装包及依赖关系pipenvgraph
生成requirements.txt文件
pipenv lock -r --dev > requirements.txt

通过requirements.txt安装环境
pipenv install -r requirements.txt

pipenv install --dev

pipenv在恢复的时候不会恢复包的依赖包

pipenv的相关使用命令
pipenv --rm         删除虚拟环境
pipenv --where          列出本地工程路径
pipenv --venv           列出虚拟环境路径
pipenv --py             列出虚拟环境的Python可执行文件
pipenv graph            查看包依赖
pipenv lock             生成lock文件
pipenv --shell          激活虚拟环境
exit                    退出虚拟环境


pipenv 只能操作当前路径下的虚拟环境







   
   

requirements.txt文件
requirements.txt文件,里面记录了当前程序的所有依赖包及版本号,其作用是用来在另一
个环境上重新构建项目所需要的运行环境依赖。
导出当前环境到requirements.txt
pip freeze >requirements.txt

使用requirements.txt恢复环境
pip install -r requirements.txt

 
 
 

"""

"""
python代码规范
1,pep8(python代码样式规范)
文档地址(中文):https://blog.csdn.net/ratsniper/article/details/78954852
2、pep257(Python文档字符串相关的约定)
文档地址: https://github.com/qiuxiang/pep/blob/master/peps/257.md
3、pep20(python的禅宗)
文档地址:https://www.python.org/dev/peps/pep-0020/


"""

"""
python之禅
优美胜于丑陋(Python以编写优美的代码为目标)
明了胜于晦涩
(优美的代码应当是明了的,命名规范,风格相似)
简洁胜于复杂(优美的代码应当是简洁的,不要有复杂的内部实现)
复杂胜于凌乱(如果复杂不可避免,那代码问也不能有难懂的关系要保持接口简洁)
扁平胜于嵌套(优美的代码应当是扁平的,不能有太多的嵌套)
问隔胜于紧凑,(优美的代码有适当的问隔,不要奢望一行代码解决问题)
可读性很重要(优美的代码是可读的)
即便假借特例的实用性之名,也不可违背这些规则(这些规则至高无上)
不要包容所有错误,除非你确定需要这样做(精准地捕获异常,不写exxcept:pass风格的代码)
当存在多种可能,不要尝试去猜测
而是尽量找一种,最好是唯一一种明显的解决方案(如果不确定,就用穷举法)
虽然这并不容易,因为你不是Python之父(这里的Dutch是指 Guido
做也许好过不做,但不假思索就动手还不如不做(动手之前要细思量)
如果你无法向人描述你的方案,那肯定不是一个好方案;反之亦然(方案测评标准)
命名空间是一种绝妙的理念,我们应当多加利用(倡导与号召)

https://docs.python.org/zh-cn/3.11/whatsnew/3.11.html  python官方文档  

"""













