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
        on = requests.get('http://192.168.188.99/admin/api.php?enable&auth=APITOKEN')
        await message.channel.send(on.text)
    if message.content == 'pi/off': #turns the blocking off
        off = requests.get('http://192.168.188.99/admin/api.php?disable&auth=APITOKEN')
        await message.channel.send(off.text)
    if message.content == 'pi/ver': #not the actual Version, only the API Version
        ver = requests.get('http://192.168.188.99/admin/api.php?version&auth=APITOKEN')
        await message.channel.send(ver.text)
    if message.content == 'pi/sum': #shows a summary of random statistics
        sum = requests.get('http://192.168.188.99/admin/api.php?summary&auth=APITOKEN')
        # pformat from pprint module, will convert json into a nicer looking string thanks random from the Internet
        await message.channel.send (pformat(sum.json()))
    if message.content == 'pi/top': #shows the top 10 domains
        top = requests.get("http://192.168.188.99/admin/api.php?topItems&auth=APITOKEN")
        await message.channel.send (pformat(top.json()))
       
        

client.run('<yourToken>')
