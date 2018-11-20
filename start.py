def start(bot, update):
    chat_id = update.message.chat_id
    text = '欢迎使用，玩的开心\n'
    text += '回复想要被投票移除的成员发送的消息，回复内容为 /kick \n'
    text += '此机器人附带删除入群退群通知 ，不要忘记给权限哦\n'
    text += '源码：<a href="https://github.com/nierunjie/adminbot">Github</a>，疯狂暗示小星星\n'
    text += '作者：@Lanthora\n'
    bot.send_message(chat_id, text,
                     parse_mode='HTML',
                     disable_web_page_preview=True)
