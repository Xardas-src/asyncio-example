from loguru import logger
from time import sleep
import asyncio


def foo_sync():
    logger.info('foo_sync starting')
    sleep(.01)
    logger.info('foo_sync finishing')


def bar_sync():
    logger.info('bar_sync starting')
    sleep(.01)
    logger.info('bar_sync finishing')


async def foo():
    logger.info('foo starting')
    await asyncio.sleep(.01)
    logger.info('foo finishing')


async def bar():
    logger.info('bar starting')
    await asyncio.sleep(.01)
    logger.info('bar finishing')


async def main_async():
    logger.info('Starting main async')
    await foo()
    await bar()
    logger.info('Finishing main async')


def main():
    # print(foo())
    # print(bar())
    # foo_sync()
    # bar_sync()
    loop = asyncio.get_event_loop()
    futures = [
        foo(),
        bar(),
    ]
    fut = asyncio.wait(futures)
    logger.info('Waiting for futures...')
    loop.run_until_complete(fut)

    # tasks = [
    #     loop.create_task(foo()),
    #     loop.create_task(bar()),
    # ]
    # tasks_wait = asyncio.wait(tasks)
    # logger.info('Waiting for tasks...')
    # loop.run_until_complete(tasks_wait)

    loop.close()


if __name__ == '__main__':
    main()
