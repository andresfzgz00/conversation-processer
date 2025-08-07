import asyncio

from src.controllers import LangChainController

async def main():
    await LangChainController.get_debt_analysis_result()


if __name__ == "__main__":
    asyncio.run(main())
