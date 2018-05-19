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
# 2018-5-19 	nongliuhua	   0.1				Original
# -----------------------------------------------------------------------*/
#
# ************************************************************************/
'''
import git
import pandas as pd
import re
from log.log_yaml import *
# log.info("aaaaaaaaaaa")
# log.debug("debug debug .....")


def get_git_data(git_path):
    '''
    使用pygit模块的相关功能获得GIT的信息，
    进如GIT所在的目录后运行得到结果
    返回结果的长字符串
    :param git_path:
    :return:
    '''
    path = git_path
    # TODO(nongliuhua):一个实际的不存在的路径 的特例处理
    # TODO(nongliuhua):一个实际的不存在.git目录的路径 的特例处理
    os.chdir(path)
    repo = git.Repo(git_path)
    # r = repo.git.log('--stat', '--date=iso')  # git log --stat  --date=iso
    r = repo.git.log( '--numstat','--date=iso')
    # print (r)
    return r


def transform_git_data_to_DataFrame(raw_git_data):
    '''
    将输入的包含git仓库信息的长字符串解析为DataFrame的数据结构
    :param raw_git_data:
    :return:
    '''
    raw_data = raw_git_data
    db_files = pd.DataFrame(columns=['commit',
                                     'author',
                                     'file_name',
                                     'commit_date',
                                     'commit_time',
                                     'insert_line',
                                     'delet_line'])

    data = raw_data.split('\n')
    i=0
    for x in data:
        if x.startswith('commit'):
            c = x.split(' ')
            commit = c[1]
        elif x.startswith('Author:'):
            c = x.split(' ')
            author = c[1]
        elif x.startswith('Date:'):
            c = x.split(' ')
            commit_date = c[3]
            commit_time = c[4]
        else:
            pattern=re.compile(r'(\d+)\s+(\d+)\s+(\S+)')
            d=re.match(pattern,x)
            if d!=None:
                insert_line=d.group(1)
                delet_line=d.group(2)
                file_name=d.group(3)
                file_dict = {'commit':commit,
                             'author':author,
                             'file_name':file_name,
                             'commit_date':commit_date,
                             'commit_time':commit_time,
                             'insert_line':insert_line,
                             'delet_line':delet_line
                             }
                db_files = db_files.append(file_dict, ignore_index=True)
    return db_files



if __name__ == '__main__':
    git_path = r'C:\Users\Administrator\Desktop\Tube_Recognize_Software'
    r = get_git_data(git_path)
    c=transform_git_data_to_DataFrame(r)



