import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import datetime
import random
import os


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['청포도 ', 'ㅊ', '청'], intents=intents)


# @client.event
# async def on_ready():
# print('Is any one there?')
# print(client.user.name)
# print(client.user.id)


playing = cycle(["청포도 도움말을 입력하시면 사용방법을 알려드립니다!", "청포도 도움말을 입력하시면 사용방법을 알려드립니다!", "적포도 게임하지 말라고", "청포도 도움말을 입력하시면 사용방법을 알려드립니다!"])

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(playing)))


@bot.event
async def on_ready():
    print(bot.user.id)
    print("ready")
    change_status.start()

@bot.event
async def on_member_join(member):
    await member.guild.system_channel.send(f'{member.mention} 님이 {member.guild.name} 서버에 입장하셨습니다')
    channel = client.get_channel(790553978122403840)
    if member.bot == False:
        bot = "유저"
    else:
        bot = "봇"
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0xff0000, title=f'{member.name}님이 서버에 입장하셨습니다')
    embed.add_field(name="**이름**", value=member.name, inline=False)
    embed.add_field(name="**서버내 별명**", value=member.display_name)
    embed.add_field(name="**디스코드 가입일**", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                    inline=False)
    embed.add_field(name="**아이디**", value=member.id)
    embed.add_field(name="**최상위 역할**", value=member.top_role.mention, inline=False)
    embed.add_field(name="**봇**", value=bot)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    return


@bot.event
async def on_member_remove(member):
    await member.guild.system_channel.send(f'{member.mention} 님이 {member.guild.name} 서버에서 퇴장하셨습니다')
    channel = client.get_channel(790553978122403840)
    if member.bot == False:
        bot = "유저"
    else:
        bot = "봇"
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0xff0000, title=f'{member.name}님이 서버에서 퇴장하셨습니다')
    embed.add_field(name="**이름**", value=member.name, inline=False)
    embed.add_field(name="**서버내 별명**", value=member.display_name)
    embed.add_field(name="**디스코드 가입일**", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                    inline=False)
    embed.add_field(name="**아이디**", value=member.id)
    embed.add_field(name="**최상위 역할**", value=member.top_role.mention, inline=False)
    embed.add_field(name="**봇**", value=bot)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    return



@bot.command(name='규칙')
async def dsbrule(ctx):
    embed = discord.Embed(color=0xFFC0, title="👥도트러 수다방 디스코드 규칙👥",
                          description="• 규칙을 제대로 읽지 않아 생긴 불상사는 저희가 책임지지 않습니다.\n• 아래 링크는 디스코드 규칙 및 운영정책. 필독 요망.",
                          url="https://discord.gg/57XGegM")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**디스코드 규칙**', value="기본적으로 `도트러 수다방 운영정책`이 적용되며 이를 어길시 주의를 받게 된다(경고X)\n\n슷칼봇 커맨드는 본인이 추가한것 외엔 건드리지 않도록 한다\n(간부진이 필요없는거 정리할때는 있음\n\n디스코드 모든곳에서 뒷담은 금지한다\n\n[📓 도트러 수다방 운영정책](https://docs.google.com/document/d/1jVtBvlR2NqQkltNpSVwZRMJIKW-4fjrg5wdaVHBMtBU/edit?usp=sharing)", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='규칙표')
async def hello(ctx):
    await ctx.send('`청포도 규칙` 이라고 말해보시는건 어떨까요?')


@bot.command(name='링크')
async def dsblink(ctx):
    embed = discord.Embed(color=0xFFC0, title="👥도트러 수다방 하위 링크👥",
                          description="• 도트러 수다방에 관련된 링크를 모아놓은 임베드입니다",
                          url="https://discord.gg/57XGegM")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='관련 링크',
              value="[📓 도트러 수다방 운영정책](https://docs.google.com/document/d/1jVtBvlR2NqQkltNpSVwZRMJIKW-4fjrg5wdaVHBMtBU/edit?usp=sharing)\n\n"
                    "[🗨 도트러 수다방 오픈채팅](https://open.kakao.com/o/gFlgUUG)\n\n"
                    "[☕ 도트러 수다방 네이버 카페](https://cafe.naver.com/gray7d0jb)\n\n"
                    "[📮 도트러 수다방 신고 및 안건제보방](https://open.kakao.com/o/geAlPH3)\n\n"
                    "[👑 도트러 수다방 간부소개서](https://cafe.naver.com/gray7d0jb/3716)\n\n"
                    "[📝 도트러 수다방 단어사전](https://cafe.naver.com/gray7d0jb/3726)\n\n"
                    "[⛏ 도트러 수다방 마인크래프트 채팅방](https://open.kakao.com/o/ggtUVNyb)\n\n"
                    "[🦆 도트러 수다방 트위터](https://twitter.com/DSbang_Gs?s=09)\n\n"
                    "[🤖 도트러 수다방 봇 제작 커뮤니티](https://discord.gg/dQgK4Hs)\n\n"
                    "[🍪 도트러 수다방 쿠키런 채팅방](https://open.kakao.com/o/gDESjkUc)", inline=False)
    await ctx.send(embed=embed)


#----------------이 밑은 채널안내-------------------------

@bot.group(invoke_without_command=True)
async def 채널안내(ctx):
        embed = discord.Embed(color=0xFFC0, title="청포도 채널안내",
                          description="도트러 수다방 디스코드 채널을 알려드려요")
        embed.set_footer(icon_url=bot.user.avatar_url, text='현재 미완성 계속 업데이트중입니다  아이스커피#1611 DM')
        embed.add_field(name='**■ 명령어 목록**', value='`청포도 채널안내 공고판`\n\n`청포도 채널안내 음성대화`\n\n`청포도 채널안내 본관`\n\n`청포도 채널안내 별관`\n\n`청포도 채널안내 기타`\n\n`청포도 채널안내 사유지`', inline=False)
        await ctx.channel.send(embed=embed)


@채널안내.command()
async def 공고판(ctx):
    embed = discord.Embed(color=0xFFC0, title="청포도 채널안내 공고판",
                          description="• 도트러 수다방 디스코드 채널을 알려드려요")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**📢『공지사항』**',value="디코 공지하는곳(쓸모없는게 대부분)", inline=False)
    embed.add_field(name='**🎉『학점평가』**', value="레벨업 정보가 올라옵니다", inline=False)
    embed.add_field(name='**🎥『cctv기록』**', value="들어온 사람을 공지합니다", inline=False)
    await ctx.channel.send(embed=embed)


@채널안내.command()
async def 음성대화(ctx):
    embed = discord.Embed(color=0xFFC0, title="청포도 채널안내 음성대화",
                          description="• 도트러 수다방 디스코드 채널을 알려드려요",)
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**[🔊] ✨『대화방』**', value="가장 기본적인 대화 음성채널", inline=False)
    embed.add_field(name='**[🔊] 📴『자습실』**', value="잠수 타는사람은 여기로 텔포", inline=False)
    embed.add_field(name='**[🔊] 🎮『피시방』**', value="게임할땐 여기서 대화!", inline=False)
    embed.add_field(name='**[🔊] 🎤『노래방』**', value="노래듣고싶다면 여기서!", inline=False)
    embed.add_field(name='**[🔊] 📶『방송실』**', value="당신의 라이브를 보여주세요!", inline=False)
    embed.add_field(name='**[🔊] 🔒『면담실』**', value="2인용으로 자유롭게 사용하시면 됩니다", inline=False)
    embed.add_field(name='**[🔊] 🗝『위클실』**',  value="3인용으로 자유롭게 사용하세요!", inline=False)
    embed.add_field(name='**[🔊] 📑『조별실』**', value="4인용으로 자유롭게 사용해주세요!", inline=False)
    await ctx.channel.send(embed=embed)


@채널안내.command()
async def 본관(ctx):
    embed = discord.Embed(color=0xFFC0, title="청포도 채널안내 도봉고 본관",
                          description="• 도트러 수다방 디스코드 채널을 알려드려요")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**📃『강의실』**', value="기본 자유 채팅방입니다!", inline=False)
    embed.add_field(name='**🎤『음악실』**', value="음악봇을 일시키는곳!", inline=False)
    embed.add_field(name='**🍴『급식실』**', value="!급식확인 내일", inline=False)
    embed.add_field(name='**🔦『당직실』**', value="**잘하자**", inline=False)
    embed.add_field(name='**🖨『인쇄실』**', value="도수방 관련 링크가 올라옵니다", inline=False)
    await ctx.channel.send(embed=embed)


@채널안내.command()
async def 별관(ctx):
    embed = discord.Embed(color=0xFFC0, title="청포도 채널안내 도봉고 별관",
                          description="• 도트러 수다방 디스코드 채널을 알려드려요")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**🕹『휴게실』**', value="모든 봇을 여기서 사용할수 있습니다!", inline=False)
    embed.add_field(name='**📉『행정실』**', value="주식하는곳! 전 운이없어요..", inline=False)
    embed.add_field(name='**🏥『보건실』**', value="마이펫은? ", inline=False)
    embed.add_field(name='**💭『어학실』**', value="단어게임들 하는곳! `끝말잇기`,`영단어퀴즈`,`훈민정음`", inline=False)
    embed.add_field(name='**📎『연구실』**', value="크시나 슷칼봇 가르치는곳!", inline=False)
    embed.add_field(name='**🖥『정보실』**', value="당신의 타자실력을 보여주세요!", inline=False)
    await ctx.channel.send(embed=embed)


@채널안내.command()
async def 사유지(ctx):

    embed = discord.Embed(color=0xFFC0, title="청포도 채널안내 사유지",
                          description="도트러 수다방 디스코드 채널을 알려드려요")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**🎣『강가』, 🎣『바다』, 🎣『호수』**', value='여기에서 낚시하세요!', inline=False)
    await ctx.channel.send(embed=embed)


@채널안내.command()
async def 기타(ctx):

    embed = discord.Embed(color=0xFFC0, title="청포도 채널안내 기타",
                          description="도트러 수다방 디스코드 채널을 알려드려요")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**📬『우체통』**', value='모든 봇의 안내가 다 여기로 와요!', inline=False)
    await ctx.channel.send(embed=embed)

#-----------------------------------------


@bot.command(name='도움말')
async def dsbhelp(message):

    embed = discord.Embed(color=0xFFC0, title="🫒 청포도 도움말 🫒",
                          description="청포도봇은 도수방 전용 챗봇입니다")
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(icon_url=bot.user.avatar_url, text='현재 미완성 계속 업데이트중입니다  아이스커피#1611 DM')
    embed.add_field(name='**■ 대화 명령어**',
                    value='`청포도 (아무말)`\n\n`청포도 반응추가❌ - 청포도의 반응을 추가합니다`\n\n`청포도 반응삭제❌ - 청포도의 반응을 삭제합니다`', inline=False)
    embed.add_field(name='**■ 안내용 명령어**', value='`청포도 규칙 - 도수방 디스코드의 규칙을 알려드립니다`\n\n`청포도 링크 - 도수방의 관련 링크에대해 알려드립니다`\n\n`청포도 채널안내 - 도수방 디스코드의 채널에 대해 알려드립니다`\n\n`청포도 내정보 - 사용자의 정보를 알려드립니다`',
                    inline=False)
    embed.add_field(name='**■ 정보 명령어**', value='`청포도 단어사전❌ - 도수방의 단어사전을 열람합니다`\n\n`청포도 기타정보❌ - 기타 정보를 알려드립니다(근데 무슨정보죠?)`',
                    inline=False)
    embed.add_field(name='**■ 관리자용 명령어**', value='`청포도 청소 (숫자)`',
                    inline=False)
    embed.add_field(name='**■ 이외 사항**', value='[아컾 봇 관리서버](https://discord.gg/eNht9Wh7X7)', inline=False)
    await message.channel.send(embed=embed)

@bot.command(name='도움')
async def dsbhelpno(ctx):
    await ctx.send('`청포도 도움말`이에요!!')

@bot.command(name='명령어')
async def dsbcommand(ctx):
        embed = discord.Embed(color=0xFFC0, title="🫒 청포도 명령어 🫒",
                          description="청포도의 모든 명령어")
        embed.set_thumbnail(url=bot.user.avatar_url)
        embed.set_footer(icon_url=bot.user.avatar_url, text='이 명령어를 사용할때는 주의해주세요  아이스커피#1611 DM')
        embed.add_field(name='**도움**', value='`규칙\n도움말\n명령어\n도움\n링크\n채널안내\n채널공고판\n채널본관\n채널별관\n채널음성대화\n채널기타\n채널사유지\n내정보\n서버정보`',inline=False)
        embed.add_field(name='**대화**', value='`안녕\n(아무말)\n잘가\n뒤져\n청포도\n적포도\n누구세요\n사탄봇\n사랑해\n배고파\n잘자\n아잉\n뭐해\n욕해줘\n선넘네\n관짝\n관짝춤\n샤인머스캣\n거봉\n도수방\n폭발\n민초\n생일`', inline=False)
        embed.add_field(name='**노래가사**', value='`노래가사\n그리워하면\n토요일밤에`', inline=False)
        embed.add_field(name='**기타**', value='`욕설표\n청소\n반응추가\n반응삭제\n광고\n디엠테스트\nㅊ\n뻘짓\n뻘짓2\n뻘짓3\n뻘짓4\n뻘짓5\n뻘짓6\n연유병\n양진\n나래\n확률\n07방\n호구와트`', inline=False)
        await ctx.channel.send(embed=embed)

@bot.command(name='내정보')
async def on_message(message):
    await message.channel.send(f'{message.author.mention}')
    user = message.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    if message.author.bot == False:
        bot = "유저"
    else:
        bot = "봇"
    date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0xFFC0, title=f'{message.author.name}의 정보')
    embed.add_field(name="**이름**", value=message.author.name, inline=False)
    embed.add_field(name="**서버내 별명**", value=message.author.display_name)
    embed.add_field(name="**디스코드 가입일**", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",
                    inline=False)
    embed.add_field(name="**아이디**", value=message.author.id)
    embed.add_field(name="**최상위 역할**", value=message.author.top_role.mention, inline=False)
    embed.add_field(name="**봇**", value=bot)
    embed.set_thumbnail(url=message.author.avatar_url)
    await message.channel.send(embed=embed)

@bot.command(name='서버정보')
async def serverinfo(ctx):
    await ctx.channel.send(f'{ctx.author.mention}')
    embed = discord.Embed(color=0xFFC0, title=f"{ctx.guild.name}의 정보",
                          description="해당 서버의 정보를 열람합니다")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(icon_url=bot.user.avatar_url, text='아이스커피#1611 DM')
    embed.add_field(name='서버 주인', value=f'{ctx.guild.owner}', inline=False)
    embed.add_field(name='서버 ID', value=f'{ctx.guild.id}', inline=False)
    embed.add_field(name='서버 인증 단계', value=f'{ctx.guild.verification_level}', inline=False)
    embed.add_field(name='서버 부스트 개수', value=f'{ctx.guild.premium_subscription_count}', inline=False)
    embed.add_field(name='서버 이모지 최대한도', value=f'{ctx.guild.emoji_limit}', inline=False)
    embed.add_field(name='서버 멤버 수', value=f'{ctx.guild.member_count}', inline=False)
    embed.add_field(name='서버 생성일', value=f'{ctx.guild.created_at}', inline=False)
    embed.add_field(name='서버 시스템채널', value=f'{ctx.guild.system_channel}', inline=False)
    embed.add_field(name='서버 기본 역할', value=f'{ctx.guild.default_role}', inline=False)
    embed.add_field(name='서버 아이콘 GiF유무', value=f'{ctx.guild.is_icon_animated}', inline=False)
    embed.add_field(name='밴', value=f'{ctx.guild.bans}', inline=False)
    embed.add_field(name='초대링크 여부', value=f'{ctx.guild.invites}', inline=False)
    await ctx.channel.send(embed=embed)


@bot.command(name='기념일')
async def holyday(ctx):
    embed = discord.Embed(color=0xFFC0, title="도수방 기념일",
                          description="도수방사람들의 생일, 도수방의 기념일입니다")
    embed.set_footer(icon_url=bot.user.avatar_url, text='문의사항 아이스커피#1611 DM')
    embed.add_field(name='**PC버전**', value='[카페 학사일정 게시판](https://cafe.naver.com/ArticleList.nhn?search.clubid=29509445&search.menuid=91&search.boardtype=L)', inline=False)
    embed.add_field(name='**모바일 버전**', value='[카페 학사일정 게시판](https://m.cafe.naver.com/ca-fe/web/cafes/29509445/menus/91)')
    await ctx.channel.send(embed=embed)


@bot.command(aliases=['청소'])
async def clean(ctx, amount:int=None):
    if ctx.author.guild_permissions.manage_messages:
        if amount == None:
            await ctx.send("`청포도 청소 (숫자)`로 사용해주세요!")
        #elif amount == str

        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"{amount}개의 메시지를 삭제했습니다!")
            channel = bot.get_channel(795225368776671252)
            user = ctx.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0xFFC0, title=f"{user.name} 님이 청소를 사용하였습니다",
                                  description="해당 사용자의 정보를 열람합니다")
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(icon_url=bot.user.avatar_url, text='아이스커피#1611 DM')
            embed.add_field(name='**서버**', value=f'서버 `{ctx.guild.name}` 에서 구동되었습니다', inline=False)
            embed.add_field(name='**채널**', value=f'채널 `{ctx.channel.name}` 에서 삭제되었습니다', inline=False)
            embed.add_field(name='**청소량**', value=f'메세지 {amount}개가 삭제되었습니다', inline=False)
            embed.add_field(name='**사용자의 가입일**', value=f'{date.year}/{date.month}/{date.day}', inline=False)
            embed.add_field(name='**사용자의 이름**', value=f'{user.name} / {user.display_name}', inline=False)
            await channel.send(embed=embed)
            return

    else:
        await ctx.send("아쉽게도... 해당 사용자는 청소를 사용할 권한이 없습니다.")
        return

@bot.command(aliases=['확률', '랜덤', '퍼센트'])
async def rdpc(ctx):
    await ctx.send(random.randint(0, 101))
    #await ctx.send('살려줘')

@bot.command(name='주사위')
async def dice(ctx):
    await ctx.send(random.choice([':one: ', ':two:', ':three:', ':four:', ':five:', ':six:']))

@bot.command(aliases=['만일'])
async def ifwhat(ctx):
    await ctx.send(random.choice(['네 확실하죠!', '전혀 아닌걸요?', '그럴수도 있겠죠?', '아마도 맞을걸요?', '아마 아닐거에요', '그럴까요?']))


@bot.command(aliases=['3주년'])
async def dsbth(ctx):
    await ctx.send(random.choice(['3주년 이벤트 참여하신분들 모두 감사드립니다!', '3주년 이벤트 맞추신분들 축하드려요! 똑똑하신 분들이네요', '부방장 여러분들도 준비하시느라 수고 많으셨습니다!']))

@bot.command(aliases=['힌트'])
async def dsbthhint(ctx):
    await ctx.send(random.choice(['흠 첫번째?\n`강의실 첫 채팅을 의미합니다`','음?', '힌트를 얻고싶나요?', '당신의 운을 믿으세요!\n`청포도 3주년 코드는 1/3 확률로 암호가 등장하죠!`', '게임이 땡기네용\n`적포도의 ~하는중 에 숨겨져있다는것을 알려주는 힌트입니다!`', '다들 운영정책 잘 지켜야해요!\n`운영정책에 숨겨진 암호에 대한 힌트입니다`', 'ㅁㄴㅇㄹ\n`방장봇 /이무말 암호에 대한 힌트입니다!`', '저도 도메인 가능하겠죠?\n`카페 등급안내에 숨겨져있다는 힌트입니다!`', '01110000011011110111001101010100001000000100011101010010010000010100111001001111010011000100110001000001\n`해석하면 포스트 그래놀라! 포스트 암호에 대한 힌트입니다`']))

#----------------이 밑은 대화-------------------------

@bot.command(aliases=['안녕', 'ㅎㅇ', '하이', '하위', '안녕하세요', '헬로', 'Hi', 'Hello', '하'])
async def chat(ctx):
    await ctx.send('안녕하세요! 반가워요!')


@bot.command(aliases=['(아무말)', '아무말', 'ㅇㅁㅁ'])
async def anysay(ctx):
    await ctx.send('그..그렇게 말구요..')

@bot.command(aliases=['잘가', 'ㅂㅇ', 'ㅂㅂ', '바이', '안녕히가세요', '바위', 'Bye', '바'])
async def bye(ctx):
    await ctx.send('안녕히가세요! 좋은 밤 되세요')

@bot.command(aliases=['뒤져', '죽어', '디져', 'ㄷㅈ', 'Die'])
async def diehaha(ctx):
    await ctx.send('...? 너무하시네요')

@bot.command(aliases=['청포도'])
async def ggrape(ctx):
    await ctx.send("저요?, 하핫 전 매우 위대한 존재랍니다!")

@bot.command(aliases=['누구세요', '후아유'])
async def whoru(ctx):
    await ctx.send('저요? 전 청포도랍니다!')

@bot.command(aliases=['사탄봇', '휴먼봇', 'SatanBot'])
async def stbot(ctx):
    await ctx.send('누구 말씀하시는지 잘 모르겠는데요..?')

@bot.command(aliases=['사랑해', '아이러브유', '사랑행', '좋아해', '조아해'])
async def iloveu(ctx):
    await ctx.send('저두요!')

@bot.command(aliases=['배고파', '헝그리'])
async def hungry(ctx):
    await ctx.send('```\n현재 업데이트 되지 않은 내용입니다\n```')

@bot.command(aliases=['잘자', '굿나잇'])
async def gnight(ctx):
    await ctx.send('안녕히주무세요!')

@bot.command(aliases=['적포도'])
async def pgrape(ctx):
    msg = await ctx.send('하 진짜 개 망할거..')
    await asyncio.sleep(0.5)
    await msg.edit(content='네? 뭐가요?')

@bot.command(aliases=['아잉', '잉아'])
async def aing(ctx):
    await ctx.send('<:Xowo:757843276073009152>')

@bot.command(aliases=['뭐해', '뭐함'])
async def wrud(ctx):
    await ctx.send(f'{ctx.message.author.mention} 님과 대화하고 있어요!')

@bot.command(aliases=['욕해줘', '욕해', '욕해봐'])
async def holyme(ctx):
    await ctx.send('제가 어떻게 욕을해요..!')

@bot.command(aliases=['선넘네'])
async def line(ctx):
    await ctx.send('죄송합니다..')

@bot.command(aliases=['관짝'])
async def coffin(ctx):
    await ctx.send('<:CD1:785427820519358475><:CD2:785427847644708886><:CD2:785427847644708886><:CD2:785427847644708886><:CD2:785427847644708886>')

@bot.command(aliases=['관짝춤'])
async def coffindance(ctx):
    await ctx.send('<:CD2:785427847644708886><:CD2:785427847644708886>\n   :coffin: \n<:CD2:785427847644708886><:CD2:785427847644708886>')


@bot.command(aliases=['샤인머스켓', '샤인머스캣'])
async def shine(ctx):
    await ctx.send('아니라구요!!! 저는 **청 포 도** 라구요!!!')

@bot.command(aliases=['거봉'])
async def biggrape(ctx):
    await ctx.send('흐흐 적포도요? ㅋㅋㅋ')

@bot.command(aliases=['도수방', '도트러수다방'])
async def dsb(ctx):
    await ctx.send('**그저 갓**')

@bot.command(aliases=['폭발', '폭8', '폭팔'])
async def boom(ctx):
    await ctx.send('<:PYB2:763751581040246785>')

@bot.command(aliases=['민트초코', '민초'])
async def mintchoco(ctx):
    await ctx.send('어으...! 별로에요..')

@bot.command(aliases=['생일', '벌스데이'])
async def btady(ctx):
    await ctx.send('제 생일은 2월 5일이에요! 마스코트가 공식적으로 생겨난 날이랍니다. 도수방의 생성일이기도 하죠!')

@bot.command(aliases=['박나래', '나래'])
async def narae(ctx):
    await ctx.send('`청포도 캐릭터` 즉 제 캐릭터를 만드신 분이에요! 부모님이죠!')


@bot.command(aliases=['양진', '양양진'])
async def yyj(ctx):
    await ctx.send('`적포도 캐릭터`를 만드신분이에요!')

@bot.command(aliases=['07', '07방'])
async def zeroseven(ctx):
    await ctx.send('흐음...그게 뭘까요 잘 모르겠네요..ㅎㅎ')

@bot.command(aliases=['ㅎㄱㅇㅌ', '호구와트'])
async def hoguwat(ctx):
    await ctx.send('음..? 무슨말인지 잘 모르겠는데요..?')
#-----------------------가르치기-----------------------



#----------------------------------------------

@bot.command(aliases=['CHHP-1'])
async def helpem(ctx):
    await ctx.send('살려주세요')

@bot.command(aliases=['CHHK-2'])
async def hack(ctx):
    await ctx.send('D')

@bot.command(aliases=['CHRD-3'])
async def thdsb(ctx):
    await ctx.send('```접근불가```')

@bot.command(aliases=['CHCR-4'])
async def carrot(ctx):
    await ctx.send('연구원이 절 협박하고있습니다')

#----------------------노래가사-----------------------

@bot.command(name='생존신고')
async def live(ctx):
    msg = await ctx.send('생존신고합니다! 살아계신분들은 손을 들어주세요!')
    await msg.add_reaction("✋")
    await asyncio.sleep(10.0)
    await ctx.send('하나.. 둘... 어...?\n(업데이트 예정)')

@bot.command(name='노래가사')
async def music1(ctx):
    await ctx.send('이 봇의 원조? 이자 김승뭔 제작한 `포도`봇에 있던 코드의 패러디입니다')

@bot.command(name='그리워하면')
async def music2(ctx):
    await ctx.send('언젠간 만나게되는')

@bot.command(name='토요일밤에')
async def music3(ctx):
    await ctx.send('바로 그날에')

@bot.command(name='토요일 밤에')#띄어쓰기 어케함
async def music4(ctx):
    await ctx.send('바로 그날에')
#----------------------------------------------




@bot.command(name='광고')
async def advertisement(ctx):
    await ctx.send('`적포도 광고`를 말해보세요!')

@bot.command(name='디엠테스트')
async def dmtest(ctx):
    await ctx.send(f'{ctx.author.mention} 디엠을 전송할게요!')
    await ctx.author.send('디엠이 도착했습니다.')

@bot.command(name='ㅊ')
async def chat1(ctx):
    await ctx.send('축하해요!')

@bot.command(name='뻘짓')
async def bchat(ctx):
    await ctx.send('<:PGB:763772550164512778>')

@bot.command(name='뻘짓1')
async def bchat1(ctx):
    await ctx.send('https://tenor.com/view/fortnite-thumbs-up-banana-thumbs-up-gif-14096917')

@bot.command(name='뻘짓2')
async def bchat2(ctx):
    await ctx.send('<:emoji_10:729974967181246467>\n<:emoji_11:729975033426083911>\n<:emoji_12:729975086383235102>')

@bot.command(name='뻘짓3')
async def bchat3(ctx):
    await ctx.send('https://tenor.com/view/star-wars-admiral-ackbar-its-atrap-trap-warning-gif-5199311')

@bot.command(name='뻘짓4')
async def bchat4(ctx):
    await ctx.send('https://tenor.com/view/knight-solar-praise-the-sun-gif-5316154')

@bot.command(name='뻘짓5')
async def bchat5(ctx):
    await ctx.send('<a:0GU1:762693900611616769>')

@bot.command(name='뻘짓6')
async def bchat6(ctx):
    await ctx.send('<:BOOM:796652353909555210>')


@bot.command(name='뻘짓7')
async def bcchat7(ctx):
    await ctx.send('<a:0WTH:817244597410332684>')


@bot.command(name='연유병')
async def yyb(ctx):
    await ctx.send('도수방 최고미인이자 아이돌, 전지전능하신 유병님을 찬양하세요!')


@bot.command(aliases=['병신', '병신아', '시발련', '씨발', '씨발련', '개새끼', '개새꺄', '개새끼야', '씨발새끼', '씨발새끼야', '미친년', '미친놈', '씹창좆병신', 'ㅅㅂ', 'ㅂㅅ', 'ㄱㅅㄲ', 'ㅅㄲ'])
async def fuck(ctx):
    await ctx.send('......ㅠㅠㅠㅠㅠㅠㅠ')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        await ctx.send(f"짜잔 오류가났습니다```\n{error}\n```")


bot.run(os.environ['token'])