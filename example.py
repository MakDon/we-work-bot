from weworkbot import bot_mgr as bots
from weworkbot import Bot as wBot

url = ""


def time_2_dinner():
    return True


# ============ hello world ====================
def hello_world():
    wBot(url).set_text("hello world").send()


# ============== 定时提醒 =======================
def foo1():
    wBot(url).set_text("every 30 seconds").every(30).run()


# ============== 带提醒人的定时提醒 ===============
def foo2():
    wBot(url)\
        .set_text("every 30 seconds")\
        .set_mentioned_list(["wangqing", "@all"])\
        .set_mentioned_mobile_list(["13800001111","@all"])\
        .every(30)\
        .run()


# ============== 带条件的定时提醒 ================
def check_something(arg1, arg2, arg3=True):
    return True


def foo3():
    wBot(url)\
        .set_text("every 30 seconds with condition")\
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'})\
        .every(30)\
        .run()


# ============== 使用函数返回消息内容 =============
def render_text(arg1, arg2, arg3=True):
    return arg1 + arg2 + arg3


def foo4():
    wBot(url)\
        .render_text(render_text, ['render', 'with'], {'arg3': 'function'})\
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'})\
        .every(30)\
        .run()


# ============== 带计数器的定时提醒 =======================
def foo5():
    # 在调用 check 5 次，或发送 3 次后停止运行
    wBot(url)\
        .set_check_counter(5)\
        .set_send_counter(3) \
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'})\
        .set_text("every 30 seconds")\
        .every(30)\
        .run()


# ============== 使用多个 bot，或同一个 bot url 多种信息 ==================
def foo6():
    # 在调用 check 5 次，或发送 3 次后停止运行
    bots.add_bot(url)\
        .set_check_counter(5)\
        .set_send_counter(3) \
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'})\
        .set_text("every 30 seconds")\
        .every(30)

    bots.add_bot(url) \
        .set_check_counter(6) \
        .set_send_counter(5) \
        .check(check_something, ['arg1', 'arg2'], {'arg3': 'arg3'}) \
        .set_text("every 10 minutes") \
        .every(minute=10)

    bots.run()
