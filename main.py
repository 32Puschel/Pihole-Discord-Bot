import discord
import requests
import json
import pprint
from discord.ext import commands
from pprint import pformat

client = commands.Bot(command_prefix = '-')
#Prefixes idk why i need this but the code breaks when I remove it. 
@client.event
async def on_ready():
    print('It works!')    

@client.event
async def on_message(message):
    if message.content == 'pi/on': #turns the blocking on
        on = requests.get('http://IpAdressofyourPI/admin/api.php?enable&auth=APIKEY')
        await message.channel.send(on.text)
    if message.content == 'pi/off': #turns the blocking off
        off = requests.get('http://IpAdressofyourPI/admin/api.php?disable&auth=APIKEY')
        await message.channel.send(off.text)
    if message.content == 'pi/ver': #not the actual Version, only the API Version
        ver = requests.get('http://IpAdressofyourPI/admin/api.php?version&auth=APIKEY')
        await message.channel.send(ver.text)
    if message.content == 'pi/sum': #shows a summary of random statistics
        sum = requests.get('http://IpAdressofyourPI/admin/api.php?summary&auth=APIKEY')
        # pformat from pprint module, will convert json into a nicer looking string thanks random from the Internet
        await message.channel.send (pformat(sum.json()))
    if message.content == 'pi/top': #shows the top 10 domains
        top = requests.get("http://IpAdressofyourPI/admin/api.php?topItems&auth=APIKEY")
        await message.channel.send (pformat(top.json()))
    if message.content == 'pi/qt': #shows the query types
        QT = requests.get('http://IpAdressofyourPI/admin/api.php?getQueryTypes&auth=APIKEY')
        await message.channel.send (pformat(QT.json()))
    if message.content == 'pi/qs': #shows the top Query Sources
        QS = requests.get('http://IpAdressofyourPI/admin/api.php?getQuerySources&auth=APIKEY')
        await message.channel.send (pformat(QS.json()))
    if message.content == 'pi/des': #shows the top Query Sources This does not work properly and I have no Idea why
        Des = requests.get('http://IpAdressofyourPI/admin/api.php?getForwardDestinations&auth=APIKEY')
        await message.channel.send (pformat(Des.json()))

        
        

client.run('Your-Bot-Token')
