from api.endpoints import get_version
import asyncio


def main() -> None:
    asyncio.run(get_version())


if __name__ == "__main__":
    main()
