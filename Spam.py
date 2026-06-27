import asyncio

member = guild.get_member(750142815811534889)

print("Waiting for user to join...")

await asyncio.sleep(10)  # wait 60 seconds

joined = member.voice is not None

if not joined:
    print("@accepted.bot")
    # send reminder message here
else:
    print("moobs on")

client.run('MTUyMDI3NDU1MzQzNDAxNzc5Mg.GwGSv4.S84qDhHKFG62LQetzNzkUslmM0ViF8cTBg5w04')