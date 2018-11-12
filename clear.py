def clear_message(bot, update):
    bot.delete_message(chat_id=update.message.chat_id,
                       message_id=update.message.message_id)
