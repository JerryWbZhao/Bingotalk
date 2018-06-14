#coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import unittest, doctest
import HTMLTestRunner, sys

sys.path.append("..")
from Bingotalk import studentSign, teacherSign

suite = doctest.DocTestSuite()

#罗列要执行的文件
suite.addTest(unittest.makeSuite(studentSign.Student))
suite.addTest(unittest.makeSuite(teacherSign.Teacher))


filename = 'D:\\bingotalkResult2.html'
fp = open(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title='Report_title',
description='Report_description')

runner.run(suite)