#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# /*-----------------------------------------------------------------------
# Copyright (C) 2017-20xx URIT Medical Electronic Co., Ltd.
# Department  		:		Research and Development Department
# Author			:		nongliuhua
# Email Address 	: 		nongliuhua@uritest.com.cn
# Filename			:		count_git.py
#  ------------------------------------------------------------------------
# Description:对放在git文件夹内的git提交信息进行工作量的统计
# -------------------------------------------------------------------------
# Modification History	:
# Data			By			   Version			Change Description
# =========================================================================
# 2018-5-18		nongliuhua	   0.1				Original
# -----------------------------------------------------------------------*/
#
# ************************************************************************/
'''
import os
import re
import sys

from log.log_yaml import *
# log.info("aaaaaaaaaaa")
# log.debug("debug debug .....")
import os

def get_git_data():
    filename_1='run_git.py'
    filename_2=r'.\data\1.txt'
    cmd='python '+filename_1+'>'+filename_2
    print(cmd)
    os.system(cmd)
    with open(filename_2, 'r',encoding='utf-8') as f:
         r = f.read()
    return r
c=get_git_data()
print(c)
print(type(c))

c=c.split('\n')
print(type(c))
print(len(c))
