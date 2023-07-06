# README 



# 项目简介

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+Allure** 通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。

## 项目说明

本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字，再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。

还可以再对接口自动化进行Jenkins持续集成。

## 源码使用说明

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令（确保当前是pip还是pip3）：

```
pip3 install -r requirements.txt
```

接着，修改 ```config/setting.ini``` 配置文件，主要配置接口域名和mysql数据库信息，pytest.ini为运行项目的相关参数。

```
testpaths-->为测试用例的文件夹
markers-->为打标签的测试用例
addopts-->为运行测试用例的参数（-q静默运行，--reruns 1失败重新运行，--alluredir ./report测试报告路径）
```

安装相应依赖之后，在命令行窗口执行命令：

```
pytest
```

**注意**：因为我这里是针对自己的接口项目进行测试，自己公司使用请重新编写测试用例

## 项目结构

- api ====>> 接口封装层，封装HTTP接口为Python接口
  - 

- config ====>> 配置文件
  - 配置host(测试域名)和mysql的相关信息

- core ====>> requests请求方法封装、关键字返回结果类
- data ====>> 测试用例数据 
  - yaml格式

- log  ====>> 存放日志文件夹
- message  ====>> 发送消息到钉钉/企业微信（需重新配置webhooks）
- report ====>> 存放测试报告文件夹
- testcases ====>> 测试用例
  - goodscenter 有关商品的测试用例
  - usercenter 有关用户的测试用例

- utils ====>> 工具类
  - 日志
  - 读取yaml中的数据
  - 响应处理
  - 

- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件

![pic1](https://cdn.staticaly.com/gh/Twistzz-XJTLU/picx-images-hosting@master/20230705/9245690a31090275cd1122ef478ab34.4xrvqflykck0.webp)

## 测试报告效果展示

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务：

```
pytest #进行pytest 

allure serve ./report
```



## 测试报告

![](https://cdn.staticaly.com/gh/Twistzz-XJTLU/picx-images-hosting@master/20230706/屏幕截图-2023-07-06-092208.6mg0d0uozjk0.webp)

![](https://cdn.staticaly.com/gh/Twistzz-XJTLU/picx-images-hosting@master/20230706/屏幕截图-2023-07-06-092233.5zgeszewbv8.webp)


通过os.environ的方式进行token的共享
