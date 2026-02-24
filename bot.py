import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

학생들 = [
    "아이비", "요나스", "에이미", "이리스", "레나",
    "한유", "민준", "쇼나", "라냐", "이온",
    "에반", "잭"
]

과목교수 = [
    "페이즐리", "사이먼", "오드리", "오웬",
    "코엔", "프레스턴", "미아", "샤를로테", "종빌런트"
]

교수전체 = [
    "페이즐리", "사이먼", "오드리", "오웬",
    "코엔", "프레스턴", "미아", "샤를로테", "종빌런트",
    "아리아", "앤"
]

@bot.command(name="학생조")
async def 학생조(ctx, 인원수: int):
    if 인원수 <= 0:
        await ctx.send("인원수는 1 이상이어야 합니다.")
        return
    목록 = 학생들[:]
    random.shuffle(목록)
    결과 = ""
    조번호 = 1
    for i in range(0, len(목록), 인원수):
        조 = 목록[i:i+인원수]
        결과 += f"{조번호}조: {', '.join(조)}\n"
        조번호 += 1
    await ctx.send(결과)

@bot.command(name="과목교수조")
async def 과목교수조(ctx, 인원수: int):
    if 인원수 <= 0:
        await ctx.send("인원수는 1 이상이어야 합니다.")
        return
    목록 = 과목교수[:]
    random.shuffle(목록)
    결과 = ""
    조번호 = 1
    for i in range(0, len(목록), 인원수):
        조 = 목록[i:i+인원수]
        결과 += f"{조번호}조: {', '.join(조)}\n"
        조번호 += 1
    await ctx.send(결과)

@bot.command(name="전체교수조")
async def 전체교수조(ctx, 인원수: int):
    if 인원수 <= 0:
        await ctx.send("인원수는 1 이상이어야 합니다.")
        return
    목록 = 교수전체[:]
    random.shuffle(목록)
    결과 = ""
    조번호 = 1
    for i in range(0, len(목록), 인원수):
        조 = 목록[i:i+인원수]
        결과 += f"{조번호}조: {', '.join(조)}\n"
        조번호 += 1
    await ctx.send(결과)

@bot.command(name="교수학생")
async def 교수학생(ctx, 학생수: int):
    if 학생수 <= 0:
        await ctx.send("학생 수는 1명 이상이어야 합니다.")
        return
    if len(학생들) == 0:
        await ctx.send("학생 목록이 비어있습니다.")
        return
    결과 = ""
    for 교수 in 과목교수:
        배정학생 = random.sample(학생들, min(학생수, len(학생들)))
        결과 += f"{교수} 조: {', '.join(배정학생)}\n"
    await ctx.send(결과)

@bot.command(name="중복학생")
async def 중복학생(ctx, 조수: int, 인원수: int):
    if 조수 <= 0 or 인원수 <= 0:
        await ctx.send("조 수와 인원수는 1 이상이어야 합니다.")
        return
    if 인원수 > len(학생들):
        await ctx.send(f"한 조 인원수는 최대 {len(학생들)}명까지 가능합니다.")
        return
    결과 = ""
    조번호 = 1
    for i in range(조수):
        조 = random.sample(학생들, 인원수)
        결과 += f"{조번호}조: {', '.join(조)}\n"
        조번호 += 1
    await ctx.send(결과)

@bot.command(name="랜덤")
async def 랜덤(ctx, 최대수: int):
    if 최대수 <= 0:
        await ctx.send("숫자는 1 이상이어야 합니다.")
        return
    멤버 = ["쿼쥐", "구리", "벌레"]
    숫자목록 = list(range(1, 최대수 + 1))
    random.shuffle(숫자목록)
    배정 = {멤버[i]: [] for i in range(len(멤버))}
    for idx, 숫자 in enumerate(숫자목록):
        배정[멤버[idx % 3]].append(str(숫자))
    결과 = ""
    for 이름, 숫자들 in 배정.items():
        결과 += f"{이름}: {', '.join(숫자들)}\n"
    await ctx.send(결과)

bot.run(os.environ.get("TOKEN"))

