import asyncio
import itertools


async def spin(msg: str):  # <1>
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)  # <2>
        except asyncio.CancelledError:  # <3>
            break
        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


async def slow():
    await asyncio.sleep(3)  # <4>
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin("thinking!"))
    print(f"spinner object: {spinner}")
    result = await slow()
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
