#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from count_backup_folder import *


def test_get_project_name_1():
    file_name = r'流式样机V0.2版矩形鞘流器测试实验报告[GH031A-2018荧光流式细胞仪研发].doc'
    a = get_project_name(file_name)
    b = '[GH031A-2018荧光流式细胞仪研发]'
    assert a == b


def test_get_project_name_2():
    file_name = r'流式样机V0.2版矩形鞘[流器测]流器测试实验报告[GH031A-2018荧光流式细胞仪研发].doc'
    a = get_project_name(file_name)
    b = '[GH031A-2018荧光流式细胞仪研发]'
    assert a == b


def test_get_project_name_3():
    file_name = r'流式样机V0.2版矩形鞘流器测流器测试实验报告GH031A-2018荧光流式细胞仪研发.doc'
    a = get_project_name(file_name)
    b = ''
    assert a == b


def test_get_project_name_4():
    file_name = r'流式样机V0.2版矩形鞘流器测流器测试实验报告【GH031A-2018荧光流式细胞仪研发].doc'
    a = get_project_name(file_name)
    b = '【GH031A-2018荧光流式细胞仪研发]'
    assert a == b


def test_get_project_name_5():
    file_name = r'流式样机V0.2版矩形鞘流器测流器测试实验报告【GH031A-2018荧光流式细胞仪研发】.doc'
    a = get_project_name(file_name)
    b = '【GH031A-2018荧光流式细胞仪研发】'
    assert a == b


def test_get_author_name_1():
    path_name = r'Z:\12 备份\17-许北林\CRP-TemperControlBoard-xubeilin-2018-05-15-幼稚细胞温控板\CMSIS'
    a = get_author_name(path_name)
    b = '许北林'
    assert a == b


def test_get_author_name_2():
    path_name = r'Z:\12 备份\17-许北林'
    a = get_author_name(path_name)
    b = '许北林'
    assert a == b


def test_get_author_name_3():
    path_name = r'Z:\12 备份\17---许北林'
    a = get_author_name(path_name)
    b = '许北林'
    assert a == b


def test_get_author_name_4():
    path_name = r'Z:\12 备份'
    a = get_author_name(path_name)
    b = ''
    assert a == b


# if __name__ == '__main__':
    # test_get_project_name_1()
    # test_get_project_name_2()
    # test_get_project_name_3()
    # test_get_project_name_4()
    # test_get_project_name_5()
    # get_author_name_1()
    # get_author_name_2()
    # get_author_name_3()
    # get_author_name_4()

# import nose2
# nose2.main()
