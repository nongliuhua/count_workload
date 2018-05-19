#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import nose
from nose.plugins.skip import SkipTest

sys.path.append('../')
from count_git import *



def test_get_git_data_1():
    # 一个实际的git仓库的路径
    git_path=r'C:\Users\Administrator\Desktop\Tube_Recognize_Software'
    a = get_git_data(git_path)
    b='commit'
    nose.tools.assert_in(b,a,msg='fail')
def test_get_git_data_2():
    raise SkipTest
    # # 一个实际的不存在的路径
    git_path=r'C:\Desktop\Tube_Recognize_Software'
    a = get_git_data(git_path)
    b='commit'
    nose.tools.assert_in(b,a,msg='fail')
def test_get_git_data_3():
    raise SkipTest
    # # 一个实际的不存在.git目录的路径
    git_path=r'C:\Desktop\Tube_Recognize_Software'
    a = get_git_data(git_path)
    b='commit'
    nose.tools.assert_in(b,a,msg='fail')



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

import nose2
nose2.main()
