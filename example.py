import asyncio
from TianGongBot import TianGongBot

# 现在存在一个严重的问题没有解决，过一段时间后Invitetoken会过期，提示等待但无法成功

TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiVS1kNzRjNWJkM2IwNDk0MmM4YTBjNDhlNjk4OTFkODBjYSIsInVzZXJfaWRlbnRpdHlfdHlwZSI6IkZyZWVVc2VyIiwidGltZXN0YW1wX21zIjoxNjg0MTQ2MDU2NjU2LCJmbXRfdGltZXN0YW1wIjoiMjAyMy0wNS0xNSAxODoyMDo1Ni42NTY1ODY1MjAiLCJyYW5kX3N0ciI6IjUxZjljZTc5NjQ3Y2I5OGMxZjI3YzQwMmZmZTg4NTNlIn0.6lgpN8pbZ-0XGWCt6Imd7mpJK8rHoLEhUcugbowfkVM"
COOKIE = "acw_tc=b640864ff056257d8f790215f72d3333ec0447d57c8a251189c0a837d96b013b"
INVITE_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJUb2tlbiI6Ikludml0ZS1kYTU0YmE2MzQwMjEyNjZjNzE4ZDRjMTMzOTE4OTYxZjRjYzRkMDY5NTQyMDQxOWY1YWU2YzRjNTEyMmM0MTQ2IiwiVXNlclR5cGUiOiJGcmVlVXNlciIsIkNoYXRRdWV1ZU51bWJlciI6NjIxOTgsIkdldE51bWJlclRpbWUiOiIyMDIzLTA1LTE1IDIzOjMzOjQ4IiwiQ3VycmVudE51bWJlcldhaXRpbmdUb1VzZSI6NjIxOTgsIkRpc3RNYXhOdW1iZXIiOjYyMTk4LCJSb3dUb051bSI6dHJ1ZSwiUm93VG9OdW1UaW1lIjoiMjAyMy0wNS0xNSAyMzozNDowOSIsIkV4dGVuZGVkUGFyYW1ldGVyT25lIjoiMTAwIiwiRXh0ZW5kZWRQYXJhbWV0ZXJUd28iOiIxIiwiRXh0ZW5kZWRQYXJhbWV0ZXJUaHJlZSI6IiJ9fQ.L5xvcT78Tc4KbDwc0zLDBXkRNsZlH5G7MQ10ZkjUFhk"
tgbot = TianGongBot.TiangongBot(COOKIE,TOKEN,INVITE_TOKEN)

async def main():
    #创建一个新的session
    session_id,message_id = await tgbot.new_session("在吗")
    #获取创建时的返回消息
    msg = await tgbot.get_msg(message_id)
    print(msg)
    #向已有的session发送消息
    message_id = await tgbot.send_msg("你是谁",session_id)
    #获取消息
    msg = await tgbot.get_msg(message_id)
    print(msg)
    
asyncio.run(main())