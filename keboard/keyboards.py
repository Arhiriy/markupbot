from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keybord = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Открыть список супов')
    keybord.add(button_1)
    return keybord

def get_keyboard_2():
    keybord_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('Отвравь фото открошки')
    button_4 = KeyboardButton('Отвравь фото куринова супа')
    button_5 = KeyboardButton('Отвравь фото борща')
    button_6 = KeyboardButton('Перейти на следуйщие блюда')
    keybord_2.add(button_3, button_4, button_5, button_6)
    return keybord_2

def get_keyboard_3():
    keybord_3 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_7 = KeyboardButton('Открыть список гарниров')
    keybord_3.add(button_7)
    return keybord_3

def get_keyboard_4():
    keybord_4 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_8 = KeyboardButton('Отвравь фото Жареной картошки')
    button_9 = KeyboardButton('Отвравь фото карбонара')
    button_10 = KeyboardButton('Отвравь фото стейка')
    button_11 = KeyboardButton('Вернутся на раздел супов')
    keybord_4.add(button_8, button_9, button_10, button_11)
    return keybord_4