from wxworkbot import bot_mgr as webo
from wxworkbot import Bot as wBot


def time_2_dinner():
    return True


if __name__ == '__main':
    wBot("")\
        .every(60)\
        .check(time_2_dinner)\
        .set_text("test")\
        .set_mentioned_list(['@all'])\
        .run()
