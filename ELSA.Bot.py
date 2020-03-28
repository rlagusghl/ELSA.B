import discord
import openpyxl
import configparser

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("TEST.Bot")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕")
    if message.content.startswith("!뭐해"):
        await message.channel.send("똥싸는중")
    if message.content.startswith("!바보"):
        await message.channel.send("멍청이")

    if message.content.startswith("!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("!뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("!언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)
        message.guild.kick()

    if message.content.startswith('!경고'):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook('경고.xlsx')
        sheet = file.active
        why = str(message.content[28:])
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author):
                sheet['B' + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send(str(author) + "경고 2회누적으로 서버에서 추방되었습니다.")
                else:
                    await message.channel.send(str(author) + "경고를 1회 받았습니다")
                    sheet["c" + str(i)].value = why
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author)
                sheet["B" + str(i)].value = 1
                sheet["c" + str(i)].value = why
                file.save("경고.xlsx")
                await message.channel.send(str(author) + "경고를 1회 받았습니다.")
                break
            i += 1

    if message.content.startswith("") and message.author.id != 693069271244210206:
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [10, 20, 30, 40, 50]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.content.send("레벨이 올랐습니다.\n현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                file.save("레벨.xlsx")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                break

            i += 1

@client.event
async def on_ready():
    a = configparser.ConfigParser()
    a.read("설정.ini")
    status = a["설정"]["상태"]
    print(client.user.id)
    print("ready")
    game = discord.Game(status)
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "??":
        await reaction.message.channel.send(user.name + "님이 중지 리액션을 하셨습니다")


@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    await client.change_presence(game=discord.Game(name='test', type=1))

@client.event
async def on_message(message):
    if message.channel.is_private and message.author.id !="693069271244210206":
        await client.send_message(discord.utils.get(client.get_all_members(), id="390823807373279233"), message.author.name + "(" + message.author.id + ") : " + message.channel)

    if message.channel.is_private and message.author.id != "693069271244210206":
        await client.send_message(client.get_channel("693334716069314580"), message.author.name + "(" + message.author.id + ") : " + message.content)

    if message.content.startswith("!DM"):
        member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
        await client.send_message(member, "ELSA봇 제작자의 답변 : " + message.content[23:])





client.run("NjkzMDY5MjcxMjQ0MjEwMjA2.Xn7OBw.W_ahccsko_FnepdfKY6Gg6eUzyM")