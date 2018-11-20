import logging
import sys

from admin_bot import AdminBot

"""
获取参数启动Bot
"""
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

if __name__ == '__main__':
    logging.info('admin bot started')
    token = sys.argv[1]
    bot = AdminBot(token)
    bot.run()
