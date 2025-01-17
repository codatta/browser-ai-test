import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig

browser = Browser(
	config=BrowserConfig(
		headless=False,
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)
controller = Controller()

async def main():
	task = (f'''Go to https://www.bitrefill.com/buy,
            choose cater's, then enter 5 dollor amount and add to cart,checkout,
            then open in Metamask,click Open in MetaMask,click 取消 in new window''')
	model = ChatOpenAI(model='gpt-4o')
	agent = Agent(
		task=task,
		llm=model,
		controller=controller,
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())