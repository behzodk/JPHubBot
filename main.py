import time
import buttons as btn
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = 'Your Token'
CHANNEL_ID = '-1001740526079'
supers = ["Behzod Musurmonqulov", "ᴀᴢɪᴢʙᴇᴋ ʙᴏʟᴛᴀʙᴏʏᴇᴠ"]
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
x = list()
@dp.message_handler(commands=["start","help"])
async def command_start(message: types.message):
    if message.from_user.full_name not in x:
        x.append(message.from_user.id)
    await bot.send_message(message.from_user.id,f"Hello, {message.from_user.full_name}\nThis bot for https://t.me/justphotohub\nYou can send your photo, video, music, book to the channel.\nCopyright: Behzod Musurmonqulov,Aziz Boltaboyev", reply_markup=btn.menu)
@dp.message_handler()
async def photo_send(message: types.message):
    if message.from_user.full_name not in x:
        x.append(message.from_user.id)
    if message.text == '📷photo':
        await bot.send_message(message.from_user.id,"Send me photo!")
        @dp.message_handler(content_types=["photo"])
        async def send_photo(message: types.Message):
            photo_id = message.photo[-1].file_id
            if message.from_user.full_name not in supers:
                await bot.send_message(message.from_user.id,f"{message.from_user.full_name} your photo will be sent after 30 seconds.Rasmingiz 30 soniyadan keyin yuboriladi!!!")
                time.sleep(30)
                await bot.send_photo(CHANNEL_ID, photo_id,
                                 caption=f"From #{message.from_user.full_name}\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo or video: @jphubbot")
                await message.reply("Thank you very much!!!")
            else:
                await bot.send_photo(CHANNEL_ID, photo_id,
                                     caption=f"From #Siyosat\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo or video: @jphubbot")
                await message.reply("Thank you very much!!!")
    elif message.text == '📹video':
        await bot.send_message(message.from_user.id, "Send me video!")
        @dp.message_handler(content_types=["video"])
        async def send_video(message: types.Message):
            if message.from_user.full_name not in supers:
                await bot.send_message(message.from_user.id,
                                       f"{message.from_user.full_name} your video will sent after 30 seconds.Videoingiz 30 soniyadan keyin yuboriladi!!!")
                time.sleep(30)
            video_id = message.video.file_id
            if message.from_user.full_name != "Behzod Musurmonqulov":
                await bot.send_video(CHANNEL_ID, video_id,
                                 caption=f"From #{message.from_user.full_name}\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo or video: @jphubbot")
                await message.reply("Thank you very much!!!")
            else:
                await bot.send_video(CHANNEL_ID, video_id,
                                     caption=f"From #Siyosat\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo or video: @jphubbot")
                await message.reply("Thank you very much!!!")
    elif message.text == '🎵music':
        await bot.send_message(message.from_user.id, "Send me music!")
        @dp.message_handler(content_types=["audio"])
        async def send_music(message: types.Message):
            music_id = message.audio.file_id
            if message.from_user.full_name not in supers:
                await bot.send_message(message.from_user.id,
                                       f"{message.from_user.full_name} your music will sent after 30 seconds. Musiqangiz 30 soniyadan keyin yuboriladi!!!")
                time.sleep(30)
                await bot.send_audio(CHANNEL_ID, music_id,
                                    caption=f"From #{message.from_user.full_name}\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo, video, music, book: @jphubbot")
                await message.reply("Thank you very much!!!")
            else:
                await bot.send_audio(CHANNEL_ID, music_id,
                                     caption=f"From #Siyosat\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo, video, music, book: @jphubbot")
                await message.reply("Thank you very much!!!")
    elif message.text == '📚Book':
        await bot.send_message(message.from_user.id, "Send me a book!")
        @dp.message_handler(content_types=["document"])
        async def send_doc(message: types.Message):
            document_id = message.document.file_id
            if message.from_user.full_name not in supers:
                await bot.send_message(message.from_user.id,
                                       f"{message.from_user.full_name} your book will sent after 30 seconds.Kitobingiz 30 soniyadan keyin yuboriladi!!!")
                time.sleep(30)
                await bot.send_document(CHANNEL_ID, document_id,
                                 caption=f"From #{message.from_user.full_name}\nSubscribe: https://t.me/justphotohub\nDou you want to send your photo, video, music, book: @jphubbot")
                await message.reply("Thank you very much!!!")
            else:
                await bot.send_document(CHANNEL_ID, document_id,
                                        caption=f"From #Siyosat\nSubscribe: https://t.me/justphotohub\nDo you want to send your photo, video, music, book: @jphubbot")
                await message.reply("Thank you very much!!!")
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
