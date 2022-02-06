from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

photobtn = KeyboardButton("📷photo")
videobtn = KeyboardButton("📹video")
musicbtn = KeyboardButton("🎵music")
bookbtn = KeyboardButton("📚Book")
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(photobtn,videobtn,musicbtn,bookbtn)
music_send_btn = KeyboardButton("Send Music")
main_btn = KeyboardButton("Main Menu")
music_send_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(music_send_btn, main_btn)
photo_send_btn = KeyboardButton("Send Photo")
photo_send_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(photo_send_btn, main_btn)
