import asyncio
import time

import websockets

# 用于构建websocket服务器，在本地8765端口启动
# 这里模拟第三方应用
IP_ADDR = "127.0.0.1"
IP_PORT = '8888'


# 握手为啥不和接受消息放一起呢 可能为了鉴权
async def serverHands(websocket):
    while True:
        recv_text = await websocket.recv()
        print(f'recv_text:{recv_text}')
        if recv_text == "hello":
            print('connected success')
            await websocket.send('hello world')
            return True
        else:
            await websocket.send("connected fail")


# 接收消息 返回消息
async def serverResv(websocket):
    while True:
        recv = await websocket.recv()
        print(f'recv:{recv}')
        await websocket.send(f"got message {recv}")


# 握手并接收数据
async def serverRun(websocket, path):
    print(path)
    await serverHands(websocket)
    await serverResv(websocket)


if __name__ == "__main__":
    print("-----server main begin--")
    server = websockets.serve(serverRun, IP_ADDR, IP_PORT)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
