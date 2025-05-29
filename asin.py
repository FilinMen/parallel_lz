import asyncio

async def error():
    await asyncio.sleep(3)
    raise ValueError("ОЙ")  

async def main():
    try:
        await error()
    except ValueError as e:
        print(f"Исключение обработано: {e}")

asyncio.run(main())