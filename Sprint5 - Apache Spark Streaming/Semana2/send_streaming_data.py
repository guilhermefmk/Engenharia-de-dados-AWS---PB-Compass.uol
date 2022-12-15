import asyncio

async def handle_echo(reader, writer):
    message = input("enter a message: ")
    data = message.encode()

    addr = writer.get_extra_info('peername')
    print(f"Sending {message!r} to {addr!r}")

    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 3456)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
