import datetime
import discord

client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('레슈야 명령어')
    await client.change_presence(status=discord.Status.online, activity=game)


# noinspection PyGlobalUndefined
@client.event
async def on_message(message):

    global voice
    if message.content.startswith("레슈야 슈하"):
        await message.channel.send("하위하위-!")

    if message.content.startswith("레슈야 레바슈보"):
        await message.channel.send("힝.. 나븐칭구!")

    if message.content.startswith("레슈야 스페셜 땡큐"):
        await message.channel.send("[LINEKING2100]( 라인킹 )님 버그 고치기 도와주셔서 고마워요!( By. Rena )")

    if message.content.startswith("레슈야 명령어"):
        user = message.author
        datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title="레슈의 명령어에요!", description="계속 추가할 예정!", color=0x62c1cc)
        embed.add_field(name="레슈야 슈하", value="레슈가 인사해줘요!", inline=True)
        embed.add_field(name="레슈야 레바슈보", value="레슈는 바부에요!(??)", inline=True)
        embed.add_field(name="레슈야 스페셜 땡큐", value="에러 고치기를 도와드린 분께 감사인사!", inline=True)
        embed.add_field(name="레슈야 정보", value=f"{user}님의 정보를 알려드려요!", inline=True)
        embed.add_field(name="레슈야 프사", value=f"{user}님의 프사를 보여드려요!", inline=True)
        embed.add_field(name="레슈야 나이", value="나이를 알려드려요!", inline=True)
        embed.add_field(name="레슈야 레슈", value="**레슈다**", inline=True)
        embed.add_field(name="레슈야 점프", value="**레슈점프!!!!!!!!!!!!!**", inline=True)
        embed.add_field(name="레슈야 청소 ( 숫자 )", value="메시지를 지워드려요!", inline=True)
        embed.add_field(name="레슈야 명령어", value="명령어를 알려드려요!", inline=True)
        embed.set_footer(text="하늘꽃 / SkyBlossom#0221")
        await message.channel.send(embed=embed)

    if message.content.startswith("레슈야 정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x46FFFF)
        embed.add_field(name="디스코드 닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="디스코드 계정 생성일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일", inline=True)
        embed.add_field(name="디스코드 아이디", value=message.author.id, inline=True)
        await message.channel.send(embed=embed)

    if message.content == "레슈야 프사":
        user = message.author
        datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{user}님의 프로필 사진이에요!")
        await message.channel.send(f"{user.avatar_url}")

    if message.content.startswith("레슈야 나이"):
        await message.channel.send("2021년 1월 11일에 만들어졌으니까.. 1살이에요!")

    if message.content.startswith("레슈야 레슈"):
        await message.channel.send("~~뭐요~~")

    if message.content.startswith("레슈야 점프"):
        await message.channel.send("뽀엥!( 점푸 )")

    if message.content.startswith("레슈야 청소"):
        number = message.content.split(" ")[2]
        await message.delete()
        await message.channel.purge(limit=int(number))
        await message.channel.send(f"{number}개의 메시지를 삭제 완료했어요!")

client.run("Nzk3OTk0ODkxNzcwNzI0Mzgy.X_ukqA.YckQ3vk9kAqzkBJGzx9Np3PKgdU")