# -*-encoding:utf-8-*-
'''
Copyright(c)2013,zhangchunsheng,www.zhangchunsheng.me
Version: 1.0
Author: zhangchunsheng
Date: 2014-03-26
Description: models
Modification:
	甲、乙、丙、丁、戊、己、庚、辛、壬、癸 甲（jiǎ）、乙（yǐ）、丙（bǐng）、丁（dīng）、戊（wù）、己（jǐ）、庚（gēng）、辛（xīn）、壬（rén）、癸（guǐ）
	子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥 子（zǐ）、丑（chǒu）、寅（yín）、卯（mǎo）、辰（chén）、巳（sì）、午（wǔ）、未（wèi）、申（shēn）、酉（yǒu）、戌（xū）、亥（hài）
	甲午年（马年）丁卯月丙申日 农历二月廿六
'''
from django.conf.urls import patterns, url;
from rankService import views;

urlpatterns = patterns('',
	# ex: /rankService/
	url(r'^$', views.index, name='index'),
	url(r'^register$', views.register, name='register'),
	url(r'^rank\?*$', views.rank, name='rank'),
	url(r'^commitScore\?*$', views.commitScore, name='commitScore')
);