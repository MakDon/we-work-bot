from weworkbot import bot_mgr as bots
from weworkbot import BotMgr
from weworkbot import Bot as wBot

url = ""


# ============ hello world ====================
def hello_world():
    wBot(url).set_text("hello world").send()


# ============ hello world ====================
def hello_world_twice():
    bot = wBot(url)
    bot.set_text('hello world').send()
    bot.set_text('<font color="info">Hello world</font>', type='markdown').send()


# ================= run ========================
def run_forever():
    # 每隔 60 秒发送一次 hello world
    # 使用Bot.every() 设置间隔
    wBot(url).set_text("hello world").run()


# ============== 定时提醒 =======================
def foo1():
    wBot(url).set_text("every 30 seconds").every(30).run()


# ============== 带提醒人的定时提醒 ===============
def foo2():
    wBot(url)\
        .set_text("every 30 seconds")\
        .set_mentioned_list(["wangqing", "@all"])\
        .set_mentioned_mobile_list(["13800001111", "@all"])\
        .every(30)\
        .run()


# ============== 带条件的定时提醒 ================
def check_something(arg1, arg2, arg3=True):
    return True


def foo3():
    wBot(url)\
        .set_text("every 30 seconds with condition")\
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'})\
        .every(30)\
        .run()


# ============== 使用函数返回消息内容 =============
def render_text(arg1, arg2, arg3=True):
    return arg1 + arg2 + arg3


def foo4():
    # 当同时调用了 render_text 与 set_text 时，优先调用 render_text
    # type 选项: 'text', 'markdown', 默认为 text
    wBot(url)\
        .render_text(render_text, args=['render ', 'with '], kwargs={'arg3': 'function'}, type='text')\
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'})\
        .every(30)\
        .run()


# ============== 带计数器的定时提醒 =======================
def foo5():
    # 在调用 check 5 次，或发送 3 次后停止运行
    wBot(url)\
        .set_check_counter(5)\
        .set_send_counter(3) \
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'})\
        .set_text("every 30 seconds")\
        .every(30)\
        .run()


# ============== 使用多个 bot，或同一个 bot url 多种信息 ==================
def foo6():
    # 在调用 check 5 次，或发送 3 次后停止运行
    bots.add_bot(url)\
        .set_check_counter(5)\
        .set_send_counter(3) \
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'})\
        .set_text("every 30 seconds")\
        .every(30)

    # 在调用 check 6 次，或发送 5 次后停止运行
    bots.add_bot(url) \
        .set_check_counter(6) \
        .set_send_counter(5) \
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'}) \
        .set_text("every 10 minutes") \
        .every(minute=10)

    bots.run()


# ============== 或创建多组 bot ==================
def foo7():

    bots1 = BotMgr()
    bots2 = BotMgr()
    bots3 = BotMgr()

    bot1 = wBot(url)\
        .set_check_counter(5)\
        .set_send_counter(3) \
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'})\
        .set_text("every 30 seconds")\
        .every(30)

    bot2 = wBot(url) \
        .set_check_counter(6) \
        .set_send_counter(5) \
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'}) \
        .set_text("every 10 minutes") \
        .every(minute=10)

    bot3 = wBot(url) \
        .set_check_counter(6) \
        .set_send_counter(5) \
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'}) \
        .set_text("every 10 minutes") \
        .every(hour=1)

    bots1.append(bot1)
    bots1.append(bot2)

    bots2.append(bot2)
    bots2.append(bot3)

    bots3.append(bot1)
    bots3.append(bot3)

    bots1.start()
    bots2.start()
    bots3.start()

    bots1.join()
    bots2.join()
    bots3.join()
