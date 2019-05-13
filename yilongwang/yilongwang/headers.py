#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

  @Time    : 19-4-28 下午2:28
  @Author  : Latent
  @Site    : 
  @File    : headers.py
  @Software: PyCharm
  @PS      : 

'''

#==> asynsearch　request

def getAsyHeaders():
    Hearders = {'Host':'hotel.elong.com',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'http://hotel.elong.com',
                'X-Request-With': 'XMLHttpRequest',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'http://hotel.elong.com/wuyishan/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
                'Cookie':'CookieGuid=f930d961-cd4b-4a29-82c0-5ca035500f3b; s_eVar44=ppzqbaidu; H5CookieId=509f2716-6855-4089-98fd-7c395428b098; _fid=f930d961-cd4b-4a29-82c0-5ca035500f3b; CitySearchHistory=1404%23%E6%AD%A6%E5%A4%B7%E5%B1%B1%23wuyishan%23; __tctma=20377580.1556154927930580.1556154927193.1556442274930.1557048044598.4; newjava1=ec4acdc2909559397e6c18445d4cf6d4; JSESSIONID=593EBC05F9CF7D6B38206ECAEE778AA0; SessionGuid=003dcc3c-1f59-4197-8e1d-c63884043fbc; Esid=accfc2ed-4a3c-4d82-a94a-259807a14da8; com.eLong.CommonService.OrderFromCookieInfo=Orderfromtype=1&Parentid=50000&Status=1&Cookiesdays=0&Coefficient=0.0&Pkid=50&Priority=8000&Isusefparam=0&Makecomefrom=0&Savecookies=0; fv=pcweb; anti_token=F18592B5-0813-4686-8B87-D01C5403CA97; ShHotel=InDate=2019-05-13&CityID=1404&CityNameEN=wuyishan&CityNameCN=%E6%AD%A6%E5%A4%B7%E5%B1%B1&OutDate=2019-05-14&CityName=%E6%AD%A6%E5%A4%B7%E5%B1%B1; ext_param=bns%3D4%26ct%3D3; s_cc=true; s_visit=1; s_sq=%5B%5BB%5D%5D; __tctmc=0.239786394; __tctmd=0.1; SHBrowseHotel=cn=01404004%2C%2C%2C%2C%2C%2C%3B92333689%2C%2C%2C%2C%2C%2C%3B41404002%2C%2C%2C%2C%2C%2C%3B01404002%2C%2C%2C%2C%2C%2C%3B90967408%2C%2C%2C%2C%2C%2C%3B&',
                'Connection':'keep-alive',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',


    }

    return  Hearders;


# ==> comment request

def getComment():
    Headers = {'Host':'hotel.elong.com',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
               'Referer': 'http://hotel.elong.com/wuyishan/',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
               'cookie':'CookieGuid=1a5141ad-936a-4fd5-af0e-f0f0f3b9cb64; _fid=1a5141ad-936a-4fd5-af0e-f0f0f3b9cb64; H5CookieId=dc458edc-c9f4-4f0e-8447-e3f462874978; CitySearchHistory=1404%23%E6%AD%A6%E5%A4%B7%E5%B1%B1%23wuyishan%23; s_eVar44=ppzqbaidu; SessionGuid=04096cc1-59c1-427e-bc63-8bf73fc7c487; Esid=4ab45dc8-35dc-4204-9267-f75fcc3d2e5b; semid=ppzqbaidu; outerFrom=ppzqbaidu; fv=pcweb; ext_param=bns%3D4%26ct%3D3; s_cc=true; __tctmu=20377580.0.0; __tctmz=20377580.1557301553088.7.1.utmccn=(organic)|utmcmd=organic|utmEsl=utf-8|utmcsr=baidu|utmctr=%e8%89%ba%e9%be%99%e7%bd%91; longKey=1556244267939716; __tctrack=0; H5SessionGuid=60d58891dcbe439497ad9bb1664a8f4f; com.eLong.CommonService.OrderFromCookieInfo=Pkid=50793&Parentid=3150&Coefficient=0.0&Status=1&Priority=9001&Makecomefrom=0&Savecookies=0&Cookiesdays=0&Isusefparam=0&Orderfromtype=5; newjava1=f83de789121602f99eca8430941e4073; anti_token=0C40D596-4F2A-4F36-817D-6843B5EB82B3; __tctmc=20377580.26050747; __tctmd=20377580.26050747; __tctma=20377580.1556244267939716.1556244395931.1557301553088.1557381543174.8; s_sq=%5B%5BB%5D%5D; SHBrowseHotel=cn=31404025%2C%2C%2C%2C%2C%2C%3B91297500%2C%2C%2C%2C%2C%2C%3B01404005%2C%2C%2C%2C%2C%2C%3B91244458%2C%2C%2C%2C%2C%2C%3B51404005%2C%2C%2C%2C%2C%2C%3B&; __tccgd=0.0; __tctmc=0.240947866; __tctmd=0.220206657; JSESSIONID=9D30BFC0D9BF81B6904DDDB762C63682; ShHotel=InDate=2019-05-12&CityID=1404&CityNameEN=wuyishan&CityNameCN=%E6%AD%A6%E5%A4%B7%E5%B1%B1&OutDate=2019-05-13&CityName=%E6%AD%A6%E5%A4%B7%E5%B1%B1; s_visit=1',
               'Connection':'keep-alive',
               'Cache-Control':'max-age=0',
               }
    return  Headers;