import discord
import os
from dotenv import load_dotenv
from solana.publickey import PublicKey
from solana.rpc.api import Client

load_dotenv()

LAMPORTS_PER_SOL = 1000000000
client = discord.Client()
solana_client = Client(os.getenv('MAINNET'))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/balance'):
        embed_var = discord.Embed(title="__Balance__", description='**{}** SOL'.format(get_balance()), color=0x2b647b)
        await message.channel.send(embed=embed_var)

    if message.content.startswith('/wallet'):
        public_key = os.getenv('PUBLIC_KEY')
        solscan = os.getenv("SOLSCAN")
        embed_var = discord.Embed(title="__Domen__", description="**ssjdao.sol**", color=0x2b647b)
        embed_var.add_field(name="__Address__", value='**{}**'.format(public_key), inline=False)
        embed_var.add_field(name="__Solscan__", value=solscan, inline=False)
        await message.channel.send(embed=embed_var)


def get_balance():
    response = solana_client.get_balance(PublicKey(os.getenv('PUBLIC_KEY')))
    return response["result"]["value"] / LAMPORTS_PER_SOL


client.run(os.getenv('TOKEN'))
