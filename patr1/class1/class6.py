# -*- coding: utf-8 -*-
# @file: class6.py
# @time: 2024 
# @user: Nemo
"""

ORM SQLAlchemy

"""

"""
3.6、ORM模型介绍
    O(objects):类和对象。I
    R(Relation):关系,关系数据库中的表格。
    M(Mapping):映射。

ORM框架的功能:
建立模型类和表之间的对应关系,允许我们通过面向对象的方式来操作数据库。

根据设计的模型类生成数据库中的表格。

通过方便的配置就可以进行数据库的切换,


数据库的字段类型
mysql常用数据类型:
    整数:int,bit
    小数:decimal(decimal表示浮点数,如decimal(5,2)表示共存5位数,小数
    字符串:varchar,char (char不可变长度,varchar可变长度)
    日期时间:date,time,datetime
    类型(enum)


类型                                          描述
Boolean Field                            布尔字段,值为True或False。
CharField(max_length=最大长度)            字符串。参数max_length表示最大字符个数。
IntegerField                                         整数





模型类案列
class TestReports(BaseTable):
    class Meta:
        verbose_name="测试报告"
        db_table = 'TestReports'
        
    report_name = models.CharField(max_length=40, null=False) 
    start_at = models.CharField(max_length=40, null=True)
    status = models.BooleanField()
    testsRun = models. IntegerField()
    successes = models. IntegerField()
    reports = models.TextField()


描述器实现ORM模型中的字段类型
    实现字符串字段



"""


class CharFiled:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value,str):
            self.value = value
        else:
            raise TypeError('need str')

    def __delete__(self, instance):
        self.value = None


class UserModel(object):
        #假设我这个是模型类
        name = CharFiled()  #   只能赋值字符串
        pwd = CharFiled()


m = UserModel()

m.name = '999'
print(m.name)



