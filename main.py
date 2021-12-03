import discord
import requests
import json
import pprint
from discord.ext import commands
from pprint import pformat

APIKEY = ' put your API Key here'
IpAddressofyourPI = "Put your Pis IP here"
Bot_Token = "Your Discord Bot Token"

client = commands.Bot(command_prefix = '-')
#Prefixes idk why i need this but the code breaks when I remove it. 
@client.event
async def on_ready():
    print('It works!')    

@client.event #pihole commands
async def on_message(message):
    if message.content == 'pi/on': #turns the blocking on
        on = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?enable&auth=' + APIKEY)
        await message.channel.send(on.text)
        print(on.text)
    if message.content == 'pi/off': #turns the blocking off
        off = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?disable&auth=' + APIKEY)
        await message.channel.send(off.text)
        print(off.text)
    if message.content == 'pi/ver': #not the actual Version, only the API Version
        ver = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?version&auth=' + APIKEY)
        await message.channel.send(ver.text)
        print(ver.text)
    if message.content == 'pi/sum': #shows a summary of random statistics
        sum = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?summary&auth=' + APIKEY)
        # pformat from pprint module, will convert json into a nicer looking string thanks random from the Internet
        await message.channel.send (pformat(sum.json()))
        print(sum.text)
    if message.content == 'pi/top': #shows the top 10 domains
        top = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?topItems&auth=' + APIKEY)
        await message.channel.send (pformat(top.json()))
        print(top.text)
    if message.content == 'pi/qt': #shows the query types
        QT = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?getQueryTypes&auth=' + APIKEY)
        await message.channel.send (pformat(QT.json()))
        print(QT.text)
    if message.content == 'pi/qs': #shows the top Query Sources
        QS = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?getQuerySources&auth=' + APIKEY)
        await message.channel.send (pformat(QS.json()))
        print(QS.text)
    if message.content == 'pi/des': #shows the top forward destinations
        Des = requests.get('http://' + IpAddressofyourPI + '/admin/api.php?getForwardDestinations&auth=' + APIKEY)
        await message.channel.send (pformat(Des.json()))
        print(Des.text)
    if message.content == 'pi/help': #shows all the Commands and what they do
        await message.channel.send ("__Here is a list of all the Commands!__"
        "\n\n**pi/on**"    
        "      this command turns the adblocking on"
        "\n**pi/off**"  
        "     This command turns the adblocking off!"
        "\n**pi/ver**"
        "    This shows the API version"
        "\n**pi/sum**"  
        "  This shows a few statistics"
        "\n**pi/top**"   
        "    This shows the top 10 most requested domains"
        "\n**pi/qt**"   
        "       this shows all the Query types and how much they are being used"
        "\n**pi/qs**" 
        "      this shows the query sources and how much they are being used"
        "\n**pi/des**"    
        "    this shows the top forward destinations"
        "\n**pi/help**" 
        "  This gives you h e l||l|| p")
        print("someone asked for help")

        
client.run("" + Bot_Token + "")
 
