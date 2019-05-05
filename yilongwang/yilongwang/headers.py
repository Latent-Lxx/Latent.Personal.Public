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
                'Cookie':'CookieGuid=1a5141ad-936a-4fd5-af0e-f0f0f3b9cb64; _fid=1a5141ad-936a-4fd5-af0e-f0f0f3b9cb64; H5CookieId=dc458edc-c9f4-4f0e-8447-e3f462874978; CitySearchHistory=1404%23%E6%AD%A6%E5%A4%B7%E5%B1%B1%23wuyishan%23; SHBrowseHotel=cn=01404036%2C%2C%2C%2C%2C%2C%3B91297500%2C%2C%2C%2C%2C%2C%3B91244458%2C%2C%2C%2C%2C%2C%3B&; SessionGuid=8dbcbca1-17bb-48a6-b1eb-7c95e1edd5a8; Esid=8624f00b-d2ad-49c2-9a63-47d3098a9d17; semid=ppzqbaidu; outerFrom=ppzqbaidu; com.eLong.CommonService.OrderFromCookieInfo=Orderfromtype=5&Parentid=3150&Status=1&Cookiesdays=0&Coefficient=0.0&Pkid=50793&Priority=9001&Isusefparam=0&Makecomefrom=0&Savecookies=0; fv=pcweb; ext_param=bns%3D4%26ct%3D3; s_cc=true; s_visit=1; s_eVar44=ppzqbaidu; __tctmc=20377580.248343553; __tctmd=20377580.232152029; __tctma=20377580.1556244267939716.1556244395931.1556442563823.1557035531308.4; __tctmb=20377580.3826517910087935.1557035531308.1557035531308.1; __tctmu=20377580.0.0; __tctmz=20377580.1557035531308.4.1.utmccn=(organic)|utmcmd=organic|utmEsl=utf-8|utmcsr=baidu|utmctr=%e8%89%ba%e9%be%99%e7%bd%91; longKey=1556244267939716; __tctrack=0; newjava1=62659afd2ede73f6fcd5c09d53222f10; JSESSIONID=4D667DEC36BD658DC201525933005CA1; anti_token=457B3B8D-B520-4FB7-A336-4706BA78D08C; ShHotel=InDate=2019-05-05&CityID=1404&CityNameEN=wuyishan&CityNameCN=%E6%AD%A6%E5%A4%B7%E5%B1%B1&OutDate=2019-05-06&CityName=%E6%AD%A6%E5%A4%B7%E5%B1%B1; __tctmb=0.1801917550695470.1557035541368.1557035541368.1; s_sq=elongcom%3D%2526pid%253Dhotel.elong.com%25252Fwuyishan%2526pidt%253D1%2526oid%253Djavascript%25253Avoid(0)%2526ot%253DA; __tccgd=0.0; __tctmc=0.213038605; __tctmd=0.189741682',
                'Connection':'keep-alive',
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',


    }

    return  Hearders;