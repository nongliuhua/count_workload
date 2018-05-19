#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# /*-----------------------------------------------------------------------
# Copyright (C) 2017-20xx URIT Medical Electronic Co., Ltd.
# Department  		:		Research and Development Department
# Author			:		nongliuhua
# Email Address 	: 		nongliuhua@uritest.com.cn
# Filename			:		count_Backup_folder.py
#  ------------------------------------------------------------------------
# Description:对放在备份文件夹内的所有员工文件进行工作量的统计
# -------------------------------------------------------------------------
# Modification History	:
# Data			By			   Version			Change Description
# =========================================================================
# 2018-5-16		nongliuhua	   0.1				Original
# -----------------------------------------------------------------------*/
#
# ************************************************************************/
'''
import os
import re
import time
import datetime
import pandas as pd
from pandas import DataFrame
import datetime

from log.log_yaml import *
# log.info("aaaaaaaaaaa")
# log.debug("debug debug .....")


def get_project_name(file_name):
    '''
    根据输入的文件名称将返回文件名称中的 项目名称
    :param file_name: XXXXXXXXXXXX[项目名称].XXX
    :return: 项目名称
    '''
    # 用正则表达式得到【】的名称
    str = file_name
    # pattern=re.compile(r'\[.*?\]')
    pattern = re.compile(r'[\[【].*?[\]】]')
    result = pattern.findall(str)
    if result:
        a = result[-1]
    else:
        a = ''
    return a
    pass


def get_author_name(path_name):
    '''
    根据输入的路径名称将返回路径中的作者名称
    :param file_name: XXXXXXXXXXXX[项目名称].XXX
    :return: 项目名称
    '''
    # 用正则表达式得到【】的名称
    str = path_name
    c = str.split('\\')
    result = c
    if len(result) > 2:
        a = result[2]
        a = a.split('-')
        a = a[-1]
    else:
        a = ''
    return a


def analysis_data():
    data_file_name = 'b.csv'
    df = pd.read_csv(data_file_name)
    # print(df[0:5])
    grouped_size=df['file_size'].groupby(df['file_author'])
    print(grouped_size.sum())
    print(grouped_size.size())



def main():
    rootdir = r"C:\Users\Administrator\Desktop\count_workload"
    rootdir = r"Z:\12 备份"
    db_files = pd.DataFrame(columns=['file_name',
                                     'file_author',
                                     'file_project_name',
                                     'file_size',
                                     'file_ctime',
                                     'file_mtime',
                                     'file_atime',
                                     'file_path',
                                     'file_count_time'])
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            # 文件作者
            file_author = get_author_name(parent)
            # 文件包含的项目名称
            file_project_name = get_project_name(filename)

            file_info = os.stat(os.path.join(parent, filename))
            # 文件大小 kb
            file_size = file_info.st_size
            # 文件创建时间  st_ctime（创建时间）
            file_ctime = file_info.st_ctime
            # 文件修改时间  st_mtime (修改时间)
            file_mtime = file_info.st_mtime
            # 文件访问时间  st_atime (访问时间)
            file_atime = file_info.st_atime
            # 文件统计的时间
            file_count_time = datetime.datetime.now()
            # print(time.localtime(file_info.st_ctime))

            file_dict = {'file_name': filename,
                         'file_author': file_author,
                         'file_project_name': file_project_name,
                         'file_size': file_size,
                         'file_ctime': file_ctime,
                         'file_mtime': file_mtime,
                         'file_atime': file_atime,
                         'file_path':parent,
                         'file_count_time': file_count_time
                         }
            db_files = db_files.append(file_dict, ignore_index=True)
    now = datetime.datetime.now()
    a = str(now.year)
    b = str(now.month)
    c = str(now.day)
    d = '_' + a + '-' + b + '-' + c
    date_csv_file_name = 'count_workload' + d + '.csv'
    date_csv_file_name='.\\data\\'+date_csv_file_name
    try:
        db_files.to_csv(date_csv_file_name)
    except BaseException:
        print('write %s wrong' % date_csv_file_name)
        print("Unexpected error:", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    main()
    pass
    # analysis_data()
