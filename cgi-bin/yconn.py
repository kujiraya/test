#!/usr/bin/env python
#-*- coding:utf-8 -*-
import cgi, urllib2, urllib
import json, base64

data = {}
guid = None
result = ""
form = cgi.FieldStorage()
code = form.getvalue("code", None)
#アプリケーションID
with open("application_id.txt", mode='r') as f:
  appid=f.readline().replace('\n', '')
call_back = "http://127.0.0.1:8000/cgi-bin/yconn.py"
if code is None:
  url = "https://auth.login.yahoo.co.jp/yconnect/v1/authorization"
  params = "?response_type=code+id_token&client_id="+appid+\
         "&scope=openid&nonce=aaddeeff&redirect_uri="+call_back
  url += params
  res = urllib2.urlopen(url)
  print res.read()

else:
  url = "https://auth.login.yahoo.co.jp/yconnect/v1/token"
  params = "grant_type=authorization_code&code="+code+"&redirect_uri="+call_back
  cred = base64.b64encode(appid + ":secret")
  para = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": call_back
  }
  para = urllib.urlencode(para)
  headers={"Authorization":"Basic "+cred,
  "Content-Type":"application/x-www-form-urlencoded;charset=URF-8"}
  try:
    req = urllib2.Request(url, para, headers)
    res = urllib2.urlopen(req)
    res = res.read()
    data = json.loads(res)
  except urllib2.HTTPError, e:
    res = json.dumps({
    "statuscode":e.code,
    "bodymessage":e.read(),
    "url":url,
    });
if "access_token" in data:
  url = "https://userinfo.yahooapis.jp/yconnect/v1/attribute?schema=openid"
  a_token = data["access_token"]
  r_token = data["refresh_token"]
  with open("access_token.txt", mode='w') as f:
    f.write(a_token)
  with open("refresh_token.txt", mode='w') as f:
    f.write(r_token)
  headers = {
    "Host": "userinfo.yahooapis.jp",
    "Authorization": "Bearer " + a_token
  }
  req = urllib2.Request(url,headers=headers)
  res = urllib2.urlopen(req).read()
  guid = json.loads(res)["user_id"]
  with open("guid.txt", mode='w') as f:
    f.write(guid)
  result = "おーけー"
print "Content-type: text/html\n"
print "<html>"
print "</body>"
print result
print "</body>"
print "</html>"
