import asyncio
from aio_TianGongClient import aio_TGClient
#注意INVITE_TOKEN持久化储存，经过一段时间后会过期，需要重新等待之后获取新的才可以使用
TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiVS1kNzRjNWJkM2IwNDk0MmM4YTBjNDhlNjk4OTFkODBjYSIsInVzZXJfaWRlbnRpdHlfdHlwZSI6IkZyZWVVc2VyIiwidGltZXN0YW1wX21zIjoxNjg0MTQ2MDU2NjU2LCJmbXRfdGltZXN0YW1wIjoiMjAyMy0wNS0xNSAxODoyMDo1Ni42NTY1ODY1MjAiLCJyYW5kX3N0ciI6IjUxZjljZTc5NjQ3Y2I5OGMxZjI3YzQwMmZmZTg4NTNlIn0.6lgpN8pbZ-0XGWCt6Imd7mpJK8rHoLEhUcugbowfkVM"
COOKIE = "acw_tc=b640864ff056257d8f790215f72d3333ec0447d57c8a251189c0a837d96b013b"
INVITE_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJUb2tlbiI6Ikludml0ZS1mOGEzOTAzZWY3N2MxNDVlYjdkZTU2MmQ5ZjRhZTU3YjYxZTI2NjYyMDNhYjc1Y2NjYmY5NjYzNjE4YzY0NDE3IiwiVXNlclR5cGUiOiJGcmVlVXNlciIsIkNoYXRRdWV1ZU51bWJlciI6NjE4OTAsIkdldE51bWJlclRpbWUiOiIyMDIzLTA1LTE1IDIxOjQxOjIxIiwiQ3VycmVudE51bWJlcldhaXRpbmdUb1VzZSI6NjE4OTAsIkRpc3RNYXhOdW1iZXIiOjYxODkwLCJSb3dUb051bSI6dHJ1ZSwiUm93VG9OdW1UaW1lIjoiMjAyMy0wNS0xNSAyMTo0MToyNCIsIkV4dGVuZGVkUGFyYW1ldGVyT25lIjoiMTAwIiwiRXh0ZW5kZWRQYXJhbWV0ZXJUd28iOiIxIiwiRXh0ZW5kZWRQYXJhbWV0ZXJUaHJlZSI6IiJ9fQ.n2-BIdaH_m5TJ9TcY0dWbvl3eF0xmKoM-tLDqqiz-Yw"

tgclient = aio_TGClient.TiangongClient(COOKIE,TOKEN,INVITE_TOKEN)

async def main():
    #创建一个新的session
    session_id,message_id = await tgclient.new_session("在吗")
    #获取创建时的返回消息
    msg = await tgclient.get_msg(message_id)
    print(msg)
    #向已有的session发送消息
    message_id = await tgclient.send_msg("你是谁",session_id)
    #获取消息
    msg = await tgclient.get_msg(message_id)
    print(msg)
    
asyncio.run(main())