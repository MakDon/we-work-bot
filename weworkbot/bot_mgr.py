from .bot import Bot


class BotMgr:

    def __init__(self):
        pass
        self.bots = []

    def add_bot(self, url):
        bot = Bot(url)
        self.bots.append(bot)
        return bot

    def run(self):
        for bot in self.bots:
            bot.start()
        for bot in self.bots:
            bot.join()


bot_mgr = BotMgr()
