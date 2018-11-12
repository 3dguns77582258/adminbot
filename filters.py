from telegram.ext import Filters


def new_and_left_filter():
    return Filters.status_update.new_chat_members | Filters.status_update.left_chat_member


status_update = new_and_left_filter()
