import discord
import asyncio
import random
import io
import requests
client = discord.Client()
mod = "Lordpigi"
adminid = "LetsDanger"
minutes = 0
hour = 0
seconds = 0
@client.event
async def on_ready():
    print('Eingeloggt als:')
    print(client.user.name)
    print("Ok alles Perfekt geklappt")
    await client.change_presence(game=discord.Game(name="auf PlayUnity"))


@client.event
async def on_message(message):
    if message.content.lower().startswith('!eingeloggt'):
        await client.send_message(message.channel, "Erfolgreich Eingeloggt!!")

    if message.content.lower().startswith('!coin'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

    if message.content.lower().startswith('!würfeln'):
        würfelaswahl = random.randint(1, 6)
        if würfelaswahl == 1:
            await client.send_message(message.channel, '1')
        if würfelaswahl == 2:
            await client.send_message(message.channel, '2')
        if würfelaswahl == 3:
            await client.send_message(message.channel, '3')
        if würfelaswahl == 4:
            await client.send_message(message.channel, '4')
        if würfelaswahl == 5:
            await client.send_message(message.channel, '5')
        if würfelaswahl == 6:
            await client.send_message(message.channel, '6')


    if message.content.startswith("!game") and message.author.name == adminid:
        game = message.content [6:]
        await client.change_presence(game= discord.Game(name = game))
        await client.send_message(message.channel, "Ich habe meinen status zu " + game + " gewechselt")

    if message.content.startswith('!uptime'):
            await client.send_message(message.channel,
                                    "`Ich bin schon {0} stunde/n {1} minuten und {3} sekunden online auf {2}. `".format(hour, minutes, message.server, seconds ))

    if message.content.startswith("!game") and message.author.name == mod:
        game = message.content [6:]
        await client.change_presence(game= discord.Game(name = game))
        await client.send_message(message.channel, "Ich habe meinen status zu " + game + " gewechselt")



    if message.content.startswith("!mobbing"):
        mober = message.author.name
        opfer = message.content [9:]
        await client.send_message(message.channel, mober + " sagt zu " + opfer + ': "DU BIST EINE RICHTIGE MISSEEEEEEDDDDDD!!!!"')

    if message.content.startswith("!beleidigung"):
        beleidigung = random.randint(1, 4)
        mober = message.author.name
        opfer = message.content [12:]
        respons = requests.get("https://t4.ftcdn.net/jpg/01/36/74/15/240_F_136741522_mRYcCID0OecwSP8BMWESQekWzf4oHV6t.jpg", stream=True)
        if beleidigung == 1:
            await client.send_message(message.channel, mober + " sagt zu " + opfer + ': "DU BIST EINE RICHTIGE MISSEEEEEEDDDDDD!!!!"')

        if beleidigung == 2:
           await client.send_message(message.channel, mober + " zeigt " + opfer + 'den MITTELFINGER')
           await client.send_file(message.channel, io.BytesIO(respons.raw.read()), filename= "bild.png")


        if beleidigung == 3:
            await client.send_message(message.channel, mober + " sagt zu " + opfer + ': "DU KLEINER BASTARD"')

        if beleidigung == 4:
            await client.send_message(message.channel, mober + " sagt zu " + opfer + ': "ICH FICKE DIR IN DEIN ANUS ABER RICHTIG"')

    if message.content.startswith("!mittelfinger"):
        opfer = message.content[14:]
        response = requests.get("https://images-na.ssl-images-amazon.com/images/I/716PxsnO4QL._SY450_.jpg", stream=True)
        await client.send_message(message.channel, "Das ist für dich " + opfer + "!!!")
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="bild.png")




async def uptime():
    await client.wait_until_ready()
    global seconds
    seconds=0
    global minutes
    minutes=0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(1)
        seconds +=1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

client.loop.create_task(uptime())
client.run("NDAxODY1ODU1NjczMzAzMDYw.DTwbAw.BYn9bYyufioWWimEsxc_51e-zUk")