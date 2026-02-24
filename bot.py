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

    # 숫자를 3명에게 균등하게 분배
    배정 = {멤버[i]: [] for i in range(len(멤버))}

    for idx, 숫자 in enumerate(숫자목록):
        배정[멤버[idx % 3]].append(str(숫자))

    결과 = ""
    for 이름, 숫자들 in 배정.items():
        결과 += f"{이름}: {', '.join(숫자들)}\n"

    await ctx.send(결과)
await bot.start("TOKEN")