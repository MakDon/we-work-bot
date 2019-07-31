import os
os.environ['PYTEST_CURRENT_TEST'] = 'True'
from weworkbot import Bot as wBot


url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fakekey"


def test_hello_world():
    msg = wBot(url).set_text("hello world").send()
    assert msg == ("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fakekey",
                   {
                    "msgtype": "text",
                    "text": {
                        "content": "hello world",
                        "mentioned_list": [],
                        "mentioned_mobile_list": []
                        }
                    }
                   )


def test_hello_world_twice():
    bot = wBot(url)
    msg1 = bot.set_text('hello world').send()
    msg2 = bot.set_text('hello world again').send()
    assert msg1 == ("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fakekey",
                    {
                        "msgtype": "text",
                        "text": {
                            "content": "hello world",
                            "mentioned_list": [],
                            "mentioned_mobile_list": []
                            }
                        }
                    )
    assert msg2 == ("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fakekey",
                   {
                    "msgtype": "text",
                    "text": {
                        "content": "hello world again",
                        "mentioned_list": [],
                        "mentioned_mobile_list": []
                        }
                    }
                   )


def is_true(arg1, arg2, arg3=True):
    return arg1 and arg2 and arg3


def test_check_true():
    msgs = wBot(url)\
        .set_send_counter(3)\
        .set_text("every 2 seconds with condition")\
        .check(is_true, args=[True, True], kwargs={'arg3': True})\
        .every(2)\
        .run()
    assert len(msgs) == 3
    assert msgs[0] == ("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fakekey",
                   {
                    "msgtype": "text",
                    "text": {
                        "content": "every 2 seconds with condition",
                        "mentioned_list": [],
                        "mentioned_mobile_list": []
                        }
                    }
                   )


def is_false(arg1, arg2, arg3=True):
    return arg1 and arg2 and arg3


def test_check_false():
    msgs = wBot(url) \
        .set_check_counter(5)\
        .set_text("every 2 seconds with condition") \
        .check(is_false, args=[True, True], kwargs={'arg3': False}) \
        .every(2) \
        .run()
    assert msgs == []
