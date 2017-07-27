# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:53:20 2014

@author: Datang
"""
import matplotlib.pyplot as plt
import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))

plt.xlabel(u'性别',fontproperties=zhfont1)
plt.ylabel(u'人数',fontproperties=zhfont1)

plt.title(u"性别比例分析",fontproperties=zhfont1)
plt.xticks((0,1),(u'男',u'女'))
rect = plt.bar(left = (0,1),height = (1,0.5),width = 0.35,align="center")

plt.legend((rect,),(u"图例",))
autolabel(rect)

plt.show()
rect = plt.bar(left = (0,1),height = (1,0.5),width = 0.35,align="center",yerr=0.000001)