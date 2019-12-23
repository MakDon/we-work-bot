# we-work-bot 
[![pipy](https://img.shields.io/pypi/v/weworkbot?color=blue)](https://pypi.org/project/weworkbot/) [![Build Status](https://travis-ci.com/MakDon/we-work-bot.svg?branch=master)](https://travis-ci.com/MakDon/we-work-bot)    
对企业微信群聊机器人进行封装以方便使用的框架  
企业微信群聊机器人官方文档点[这里](https://work.weixin.qq.com/api/doc#90000/90136/91770)   
鹅厂同学的加料版企业微信机器人可以参考 [wxwork_robotd](https://github.com/owt5008137/wxwork_robotd) 和 [DiaoBot](https://github.com/Bokjan/DiaoBot)

## Dependencies  
Python 3.5+   
requests

## Install

`pip3 install weworkbot`

## Quick Start

    from weworkbot import Bot as wBot
    
    wBot(url).set_text("hello world").send()
    wBot(url).set_text('<font color="info">Hello world</font>', type='markdown').send()
    wBot(url).set_image_path('test.jpeg').send()
## 更多例子

封装了定时任务、提醒列表、发送计数等功能，详见[examples](https://github.com/MakDon/we-work-bot/blob/master/example.py)

## 更新计划

- [x] 添加单测以及 Travis CI 配置
- [x] 添加 Markdown 类型消息的支持
- [x] 添加 image 类型消息的支持
- [ ] 添加 CLI 支持
- [ ] 添加 图文类型消息的支持

## Contributing

如果有使用上的问题、需要新功能、或发现了 bug，请[创建新 issue](https://github.com/MakDon/we-work-bot/issues)    
或直接[提交 pull request](https://github.com/MakDon/we-work-bot/pulls)

## License

MIT License
