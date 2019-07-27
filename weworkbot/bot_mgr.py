from .bot import Bot
from threading import Thread


class BotMgr(Thread):

    def __init__(self):
        super(BotMgr).__init__()
        self.bots = []

    def add_bot(self, url):
        assert isinstance(url, str)
        bot = Bot(url)
        self.bots.append(bot)
        return bot

    def run(self):
        for bot in self.bots:
            bot.start()
        for bot in self.bots:
            bot.join()

    def append(self, bot):
        assert isinstance(bot, Bot)
        self.bots.append(bot)


bot_mgr = BotMgr()
