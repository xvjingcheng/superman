# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。
# （2）请使用 APIID 及 APIKEY来调用接口，可在会员中心获取；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client

import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
account = "C45031386"
# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
password = "481af8a3a877b0275d0adb91d0d7fdae"


def send_sms(text, mobile):
    # 发送短信的参数
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    # 请求头信息
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # 构建链接对象
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    # 发起请求
    conn.request("POST", sms_send_uri, params, headers)
    # 收到回复
    response = conn.getresponse()
    # 读取回复信息
    response_str = response.read()
    # 关闭本次访问
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "18937012800"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))
