# we-work-bot 
![pipy](https://img.shields.io/pypi/v/weworkbot?color=blue) [![Build Status](https://travis-ci.com/MakDon/we-work-bot.svg?branch=master)](https://travis-ci.com/MakDon/we-work-bot)    
对企业微信群聊机器人进行封装以方便使用的框架  
企业微信群聊机器人官方文档点[这里](https://work.weixin.qq.com/api/doc#90000/90136/91770)  

## dependencies  
Python 3.5+   
requests

## Install

`pip3 install weworkbot`

## Quick Start

    from weworkbot import Bot as wBot
    def hello_world():
        bot = wBot(url).set_text("hello world").send()
        
## 更多例子

封装了定时任务、提醒列表、发送计数等功能，详见[examples](https://github.com/MakDon/we-work-bot/blob/master/example.py)

## 更新计划

- [ ] 添加单测以及 Travis CI 配置
- [ ] 添加 Markdown 类型消息的支持
- [ ] 添加 image 类型消息的支持
- [ ] 添加 图文类型消息的支持

## Contributing

如果有使用上的问题、需要新功能、或发现了 bug，请[创建新 issue](https://github.com/MakDon/we-work-bot/issues)    
或直接[提交 pull request](https://github.com/MakDon/we-work-bot/pulls)

## License

MIT License
