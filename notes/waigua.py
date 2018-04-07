# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 03:28:14 2017

@author: LiuWeipeng
"""


#from pywinauto.application import Application
#app = Application().Start(cmd_line=u'"C:\\Program Files\\\u7a0b\u5e8f\u5316\u4ea4\u6613\u914d\u5957\u8f6f\u4ef6\\xiadan.exe" ')
#afxb = app[u'\u7f51\u4e0a\u80a1\u7968\u4ea4\u6613\u7cfb\u7edf5.0']
#afxb.Wait('ready')
#button = afxb[u'\u5168\u64a4(Z /)']  #全撤
import pywinauto
import sys
from time import sleep
app = pywinauto.application.Application()
app.connect(title='网上股票交易系统5.0')
top_hwnd = pywinauto.findwindows.find_window(title='网上股票交易系统5.0')
dialog_hwnd = pywinauto.findwindows.find_windows(top_level_only=False, class_name='#32770', parent=top_hwnd)[0]
wanted_hwnds = pywinauto.findwindows.find_windows(top_level_only=False, parent=dialog_hwnd)           
dialog_window =app.window_(handle=dialog_hwnd)

dialog_window['全撤(Z /)'].Click() 
sleep(0.5)
Dlg=app.top_window_()
try:
    Dlg['是'].Click()
except:
    Dlg['确定'].Click()
treewin=app.top_window().window(control_id=129,class_name='SysTreeView32')
treewin.get_item(['查询[F4]', '资金股票']).click()
treewin.select(['双向委托[F6]'])
treewin.select(['查询[F4]', '资金股票'])
treewin.select(['新股申购', '批量新股申购'])
c=treewin.print_items()

stdout = sys.stdout  #以下开始保存打印结果
class TextArea(object):
        def __init__(self):
                self.buffer = []
        def write(self, *args, **kwargs):
                self.buffer.append(args)
sys.stdout = TextArea()  #申请的空间
treewin.print_control_identifiers()

dialog_window.print_control_identifiers() #打印控件信息
data = pywinauto.clipboard.GetData() #粘贴
text_area, sys.stdout = sys.stdout, stdout #获取控件信息
mes=text_area.buffer
f=open('kongjian.txt','w')
for i in mes:
    k=' '.join([str(j) for j in i])
    f.write(k+"\n")
f.close()
dialog_window.Static19.WindowText()

rect = dialog_window.CCustomTabCtrl.ClientRect()
x = rect.width()
y = rect.height()//2
x = int(x // 10)
dialog_window.CCustomTabCtrl.ClickInput(coords=(x, y))
sleep(1)
#dialog_window.SetFocus()
dialog_window.Button5.DoubleClick()  
dialog_window.Button6.Click()  
dialog_window['撤卖(C)'].Click() 
dialog_window['撤买(X)'].Click() 
dialog_window['全撤(Z /)'].Click() 

holding=data.split('	')
holding.pop()

codes=holding[:: 15]
codes.pop()
codes.pop(0)
num=holding[12 :: 15]  #实际数量
num.pop(0)


