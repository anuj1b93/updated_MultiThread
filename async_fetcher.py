import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def crawl_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def fetch_and_parse(urls):
    """Fetch and parse HTML content from multiple URLs."""
    html_pages = asyncio.run(crawl_urls(urls))
    return [parse_html(html) for html in html_pages]

