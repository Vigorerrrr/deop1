# -*- coding: utf-8 -*-
# @file: demo_60.py
# @time: 2024 
# @user: Nemo
# singleton.py

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
