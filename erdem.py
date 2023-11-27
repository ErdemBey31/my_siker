from pyrogram import Client, filters

import random

auto_reply = True

alfabe = "abcçdefgğıijklmnoöprsştuvyz"

bot = Client("botiss", api_id=24588661, api_hash="332058c74190c9a3739f43676f3a21e0", session_string="AQFxEJUAJ5o7Kr9XZVEPHY6fcblA6us4Am0LB_XHOjygIAp4_SsNJQvaUVu_UklGpkEyTjCCjS_ypnEgjjbM9ofzon7sdGxUa_1LKICZ2F-cP8ehQupYCIOtdyFbQKbmAdlUz-C140FH65erKS-QoajFErFO8JuBfZmWfF8Qz-qp8h1gYyUlOG7bQYYIMYyOIJ4uTgYOmecMPDbHdfeKxgH747nR5Fymrb_-uVczflmttYFA-7laMH_Jq2sV8k1n_IiBhJgShEjDWcu1USXox-TmjKADYfbKXduB9FUw7XP8-EY-N74wrT_T6WeUN-AyPpWNwfNBqVUZ377dmw8cGqF8cOm3LAAAAAGHUbgHAA")

@bot.on_message(filters.text)

def boton(client, message):

  global auto_reply


  chattype = message.chat.type

  if chattype == "channel" or chattype == "private":

    return

  if "ilk" in message.text.replace("İ", "i").lower():

    if message.forward_from_chat and "-100" in  str(message.forward_from_chat.id):

      if auto_reply == False:

        return
      

      text = message.text.replace("İ", "i").lower();

      words = text.split()

      try:

        index_start = words.index("ilk")

        index_end = words.index("yazana")

        keywords = words[index_start + 1:index_end]    

        message.reply(" ".join(keywords))

        bot.send_photo(chat_id="vpnteam32", photo="https://telegra.ph/file/c23d5fc6e3b884a25d430.jpg", caption="**𝗬𝗘𝗡𝗜 𝗜𝗟𝗞 𝗬𝗔𝗭𝗔𝗡:**\n\n**Gruᴩ ᴋiʍligi:** `{}`\n\n**Gruᴩ isʍi:** {}".format(message.chat.id, message.chat.title))

      except:

        if "yazan" in message.text.lower() and message.forward_from_chat:

          print(f"{message.chat.title} Grubunda  ilk yazan yapıldı.")

          if "-100" in str(message.forward_from_chat.id):
          
            if auto_reply == False:

              return
            message.reply("".join(random.sample(alfabe, k=2)))

            bot.send_photo(chat_id="vpnteam32", photo="https://telegra.ph/file/c23d5fc6e3b884a25d430.jpg", caption="**𝗬𝗘𝗡𝗜 𝗜𝗟𝗞 𝗬𝗔𝗭𝗔𝗡:**\n\n**Gruᴩ ᴋiʍligi:** `{}`\n\n**Gruᴩ isʍi:** {}".format(message.chat.id, message.chat.title))

  elif message.text.startswith(".cevapla") and message.from_user.id == 6954738598: 

    

    textsp = message.text.split()

    if len(textsp) > 1:

      if textsp[1].lower() == "on":

        auto_reply = True

        message.reply("**İlk yazan toplama aktif edildi**.")

      elif textsp[1].lower() == "off":

        auto_reply = False

        message.reply("**İlk yazan toplama devre dışı**.")

        

  

  

  

bot.run()