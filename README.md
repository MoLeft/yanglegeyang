# yanglegeyang
利用代理服务器让羊了个羊每一关都是第一关，亲测局域网范围全都进羊圈了
# 原理
利用mitmproxy创建代理服务器，自定义拦截脚本(interceptor.py)修改关卡，让每一关都变成第一关
# 教程
1.安装mitmproxy，很简单，亲测centos7.6和raspberry pi完美安装
```shell
pip3 install mitmproxy
```
2.先启动一下mitmproxy，让他生成ca证书，然后ctrl+c就行了
```shell
mitmdump -s interceptor.py
```
3. 复制ca证书到手机，自行安装，不多讲
```shell
证书在：~/.mitmproxy/mitmproxy-ca-cert.pem
```
4. 启动mitmproxy
```shell
mitmdump -q -p 23456 -s interceptor.py
```
5. 在手机上设置代理服务器，打开游戏，不出意外，就可以把每一关都改成第一关了
> 代理服务器ip: 内网ip
> 
> 代理服务器端口:23456
# Tips
发现有的手机需要把ca证书安装到系统证书里面才可以用，具体步骤大家百度吧，可以利用root也可以利用magisk模块
# 效果
![db7732b11e6e0709baf2588b2e871a3](https://user-images.githubusercontent.com/41848811/190659574-7b1c4af8-f68e-4d2f-93d6-cff693871005.png)
