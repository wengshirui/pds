# 网络问题
import asyncio
import websockets

IP_ADDR = "127.0.0.1"
IP_PORT = '8888'


# 向服务器握手
async def clientHands(websocket):
    while True:
        await websocket.send('hello')
        response_str = await websocket.recv()
        if 'hello world' in response_str:
            print('connected success')
            return True
        else:
            print('connected fail')


# 向服务器发送消息
async def clientSend(websocket):
    while True:
        input_text = input('请输入：')
        if input_text == 'exit':
            print(f'exit,bye!')
            await websocket.close(reason="exit")
        else:
            await websocket.send(input_text)
            recv_text = await websocket.recv()
            print(f'{recv_text}')


# 进行websocket连接
async def clientRun():
    ipdress = f'ws://{IP_ADDR}:{IP_PORT}'
    async  with websockets.connect(ipdress) as websocket:
        await clientHands(websocket)
        await clientSend(websocket)


if __name__ == "__main__":
    print("-----client main begin--")
    asyncio.get_event_loop().run_until_complete(clientRun())
