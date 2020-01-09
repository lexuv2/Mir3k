from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord
import time
from googletrans import Translator
import random
from chatterbot.trainers import ListTrainer
from fbchat import Client
from fbchat import Client, ThreadType, Message, ImageAttachment, TypingStatus, MessageReaction, ThreadColor
import threading
import logging
# from fbchat import log
from chatterbot.response_selection import get_most_frequent_response
import chatterbot.conversation
import time
import datetime
import urllib.request
from requests import get
import chatterbot.comparisons
import praw
import requests
import os
import random
from chatterbot import filters
import asyncio

bot = ChatBot('Ron Obvious',  # response_selection_method=get_most_frequent_response,
              filters=["chatterbot.filters.RepetitiveResponseFilter", filters.get_recent_repeated_responses],
              logic_adapters=[
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "statement_comparison_function": chatterbot.comparisons.levenshtein_distance
                  },
              ])  # Ron Obvious - pierwszy bot

# Create a new trainer for the chatbot
trainer = ListTrainer(bot)

TOKEN = 'NTEzMTA0NDI4ODYyMDEzNDQx.DtDJSg.Ch7NaVVpN-qqGDPYC3bRWf0rwCs'

client = discord.Client()

teksty = ["Daj mi chwileczke",
          "Już piszę",
          "Jak skończę jeść",
          "Ok poczekaj chwilę",
          "Wołam Mickiewicza 5 minut",
          "Niech ci będzie",
          "Za chwilę wyślę",
          "Kurwa nie przeszkadzaj mi jełopie",
          "Daj chwile tylko dopije sok z gumijagód",
          "Kurwa spokojnie",
          "...",
          "Dobra, dobra",
          "Wołam dimke",
          "Już prawie skończyłem"]

malpa = ["Spadaj",
         "Kurwa mać zamknij ryj",
         "Spierdalaj cioto",
         "a masz zgode od rodzica?",
         "hahaha",
         "wypierdalaj",
         "Czego kurwa przeszkadzasz gówniarzu, wypierdalaj stond."]

samogloski = ['a', 'e', 'u', 'o', 'i', 'y']


def download(url, file_name):
    # open in binary mode
    print("funkcyja")
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)


def learn(pyt, odp):
    global bot
    msgs[0] = pyt
    msgs[1] = odp
    print("ucze się z " + str(msgs[0] + "->" + str(msgs[1])))
    trainer = ListTrainer(bot)
    print(trainer.train(msgs))


def translate(a):
    t = Translator()

    k = ["爱", "性", "女", "恋", "玫", "红", "美", "所", "你", "酒", "吻", "我", "马", "热", "体", "紫", "乳", "您", '教', '皇', '强', '奸',
         '像', '许', '多', '没', '什', '么', '案件', '痛', '苦', '我', '急', '因', '为', '您', '教皇', '存', '在', '胎', '儿', '法', '案', '棒',
         '豆', '类', '黑', '白', '液体', '液', '体', '萧', '条', '射', '从', '前', '是', '有', '先进', '先', '进', '象', '凶手', '手', '丁',
         '七', '万', '丈', '三', '上', '下', '不', '丑', '专', '世', '丘', '业', '丛', '东', '丝', '丟', '丢', '两', '两', '严', '丧', '个',
         '中', '丰', '串', '临', '丸', '丹', '为', '主', '丽', '举', '乃', '久', '么', '义', '之', '乌', '乎', '乏', '乐', '乒', '乓', '乔',
         '乗', '乘', '九', '也', '习', '乡', '书', '买', '乱', '乳', '乾', '亂', '了', '予', '争', '事', '二', '于', '亏', '云', '互', '五',
         '井', '亚', '些', '亞', '亡', '交', '亥', '亦', '产', '亨', '亩', '享', '京', '亭', '亮', '亲', '亷', '人', '亾', '亿', '什', '仁',
         '仅', '仆', '仇', '今', '介', '仍', '从', '仑', '仓', '仔', '仕', '他', '付', '仙', '仝', '代', '令', '以', '仪', '们', '仰', '仲',
         '件', '价', '任', '份', '仿', '企', '伊', '伍', '伏', '伐', '休', '众', '优', '伙', '会', '伞', '伟', '传', '伤', '伦', '伪', '伯',
         '估', '伴', '伸', '伺', '似', '伽', '但', '佈', '位', '低', '住', '佐', '佑', '体', '佔', '何', '余', '佛', '作', '佢', '佣', '佩',
         '佳', '使', '來', '侈', '例', '侍', '侖', '供', '依', '侠', '侣', '侦', '侧', '侨', '侯', '侵', '侶', '侷', '便', '係', '促', '俄']
    defaultlan = 'pl'
    if ((len(k) - len(set(k))) > 0):  # check duplicates
        print('[Warning] there are duplicates in your table')
    a = int(a)

    w = '我'
    for i in range(0, a):
        w = w + random.choice(k) + ' '
    w = t.translate(w, src='zh-CN', dest=defaultlan).text
    for i in range(0, random.randint(0, 10)):
        w = t.translate(w, dest='pa').text
        w = t.translate(w, dest='ja').text
    w = t.translate(w, dest=defaultlan).text

    return str(w)


def licz_sylaby(x):
    sylaby = []
    for i in range(0, len(x) - 1):
        sylaby.append(0)
        sylaby.append(0)
        for j in range(0, len(x[i]) - 1):
            if x[i][j] in samogloski:
                sylaby[i] += 1
    return sylaby


def szukaj_rymow(x):
    w = ""
    jedynki = []

    x = x.split()
    sl = licz_sylaby(x)
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if len(x[i]) > 4 and len(x[j]) > 4:
                if str(x[i][len(x[i]) - 1]) == str(x[j][len(x[j]) - 1]) and str(x[i][len(x[i]) - 2]) == str(
                        x[j][len(x[j]) - 2]) and str(x[i][len(x[i]) - 3]) == str(x[j][len(x[j]) - 3]) and str(
                    sl[i]) == str(sl[j]):
                    if str(x[i]) != str(x[j]) and (not (str(x[i]) + " " + str(x[j]) in w)) and (
                            not (str(x[j]) + " " + str(x[i]) in w)) and x[i] != x[j]:
                        for k in range(0, len(x) - 1):
                            for l in range(0, len(x) - 1):
                                if x[k] != x[l] and sl[k] + sl[i] == sl[j] + sl[l]:
                                    if not x[k] in jedynki:
                                        if not x[i] in w:
                                            if not x[j] in w:
                                                jedynki.append(x[k])
                                                jedynki.append(x[l])
                                                pierwsze = x[k]
                                                drugie = x[l]
                                                w += pierwsze
                                                w += " "
                                                w += x[j]
                                                w += "\n"
                                                w += drugie
                                                w += " "
                                                w += x[i]
                                                w += "\n"
                                                w += "\n"

    return w


lastmsg = ""
msgs = []
msgs.append(" ")
msgs.append(" ")

arr = []
color = False
f = open("l_mute".txt", "a+")

class EchoBot(Client):

    async def on_message(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=None, at=None,
                         metadata=None, msg=None):
        print('paapakj')
        await self.set_typing_status(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)

        talk = False
        
  with open("l_mute.txt") as f:
      if (thread_id in f.read()):
          if ("!mute" in str(message_object.text)):
              with open("l_mute.txt", "r") as f:
                  lines = f.readlines()
              with open("l_mute.txt", "w") as f:
                  for line in lines:
                      if line.strip("\n") != thread_id:
                          f.write(line)
              await self.send(Message(text="w końcu moge gadać"), thread_id=thread_id, thread_type=thread_type)
          else:
              pass
      else: 
        if (len(message_object.attachments) > 0) and message_object.text == None:
            talk = True
            for img in message_object.attachments:
                url = await self.fetch_image_url(str(img.uid))
                response = requests.get(url).content
                with open("memy/" + str(time.time()) + ".jpg", 'wb') as file:
                    file.write(response)
            path = "memy/"
            files = os.listdir(path)
            index = random.randrange(0, len(files))
            upload = files[index]
            await self.send_local_files("memy/" + str(upload), bot.storage.get_random(), thread_id=thread_id,
                                        thread_type=thread_type)
         
            if ("!mute" in str(message_object.text)):
                    f.write(thread_id)
                    await self.send(Message(text="juz sie robi panie"), thread_id=thread_id, thread_type=thread_type)
                    
            if ('!memy' in str(message_object.text)):
                first = str(message_object.text)
                first = first.replace("!memy", '')
                path = "memy/"
                talk = True
                if int(first) <= 10:
                    for x in range(0, int(first)):
                        files = os.listdir(path)
                        index = random.randrange(0, len(files))
                        upload = files[index]
                        await self.send_local_files("memy/" + str(upload), bot.storage.get_random(), thread_id=thread_id,
                                                    thread_type=thread_type)
                else:
                    await self.send(Message(text="spadaj za dużo"), thread_id=thread_id, thread_type=thread_type)

            if (str(message_object.text) == '!sentencja'):
                msg = str(teksty[random.randint(0, len(teksty) - 1)])
                await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                msg = translate(50)
                await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                talk = True

            if (str(message_object.text) == '!wiersz'):
                msg = str(teksty[random.randint(0, len(teksty) - 1)])
                await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                msg = szukaj_rymow(translate(400))
                await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                talk = True

            if (("kocham" or "Kocham") in str(message_object.text).lower()):
                info = await self.fetch_user_info(author_id)
                info = info[str(author_id)]
                await self.send(Message(text="ja ciebie również " + str(info.name) + " <33"), thread_id=thread_id,
                                thread_type=thread_type)
                await self.reactToMessage(message_object.uid, MessageReaction.LOVE)
                talk = False

            if ('!twardo' in str(message_object.text)):
                # global bot
                if author_id == "100007449961234" or author_id == "100010187023438":
                    first = str(message_object.text)
                    first = first.replace("!twardo", '')
                    first = first[1:]
                    try:
                        # print(help(bot.storage))
                        bot.storage.remove("test")
                        msg = "chyba zadziałało"
                        await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                    except Exception as e:
                        await self.send(Message(text=str(e)), thread_id=thread_id, thread_type=thread_type)
                    talk = True
                else:
                    msg = malpa[random.randrange(0, len(malpa))]
                    await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                    talk = True

            if ('!dajadmina' in str(message_object.text)):
                await self.send(Message(text="wysłałem do stwórcy prośbe o admina"), thread_id=thread_id,
                                thread_type=thread_type)
                await self.send(Message(text=str(author_id) + " " + "chce admina"), thread_id=100007449961234,
                                thread_type=ThreadType.USER)
                talk = True

            if ('!baza' in str(message_object.text)):
                first = str(message_object.text)
                first = first.replace("!twardo", '')
                first = first[1:]
                msg = ''
                for x in range(0, 100):
                    msg += '['
                    msg += str(bot.storage.get_random())
                    msg += ']'
                    msg += '\n'

                await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                talk = True

            if ('!licz' in str(message_object.text)):
                await self.send(Message(text=bot.storage.count()), thread_id=thread_id, thread_type=thread_type)
                talk = True

            await self.mark_as_delivered(thread_id, message_object.uid)
            await self.mark_as_read(thread_id)

            # If you're not the author, echo
            if author_id != self.uid and talk == False:
                react = random.randint(0, 20)
                if react == 0:
                    await self.react_to_message(message_object.uid, MessageReaction.LOVE)
                if react == 1:
                    await self.react_to_message(message_object.uid, MessageReaction.ANGRY)
                if react == 2:
                    await self.react_to_message(message_object.uid, MessageReaction.NO)
                if react == 3:
                    await self.react_to_message(message_object.uid, MessageReaction.SAD)
                if react == 4:
                    await self.react_to_message(message_object.uid, MessageReaction.SMILE)
                if react == 5:
                    await self.react_to_message(message_object.uid, MessageReaction.WOW)
                if react == 6:
                    await self.react_to_message(message_object.uid, MessageReaction.YES)

                inputer = str(message_object.text)
                inputer = inputer.replace("@Mirek Gajos", '')
                out = str(bot.get_response(inputer))
                msg = str(out)
                await self.send(Message(text=msg), thread_id=thread_id, thread_type=thread_type)
                txtt = str(message_object.text)
                t = threading.Thread(target=learn(out, txtt))
                t.start()

            await self.set_typing_status(TypingStatus.STOPPED, thread_id=thread_id, thread_type=thread_type)


loop = asyncio.get_event_loop()


async def start():
    client = EchoBot(loop=loop)
    print("Logging in...")
    await client.start('kryptomail12345@gmail.com', 'Aleks@2003')
    print("xalo")
    client.listen()


loop.run_until_complete(start())
loop.run_forever()

# logging.basicConfig(level=logging.INFO)
