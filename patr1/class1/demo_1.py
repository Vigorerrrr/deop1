# -*- coding: utf-8 -*-
# @file: demo_1.py
# @time: 2024 
# @user: Nemo
class ToolUtil(object):
    def __init__(self, name):
        self.name = name

    def do_cupboard(self):
        print("{} 能打开柜子".format(self.name))

    def do_screw(self):
        print("{} 能拧螺丝".format(self.name))


tool_util = ToolUtil(name="工具集")


