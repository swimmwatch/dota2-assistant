import asyncio
import json
from pprint import pprint
import websockets
from loguru import logger
import argparse


async def echo(websocket):
    async for message in websocket:
        json_data = json.loads(message)
        pprint(json_data)


async def main(args):
    async with websockets.serve(echo, args.host, args.port):
        logger.info(f'Websocket server running on: {args.host}:{args.port}')
        await asyncio.Future()  # run forever


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--host', type=str, required=True, help='Hostname')
arg_parser.add_argument('--port', type=int, required=True, help='Port')
args = arg_parser.parse_args()

try:
    asyncio.run(main(args))
except KeyboardInterrupt:
    logger.info('Shutdown server.')
