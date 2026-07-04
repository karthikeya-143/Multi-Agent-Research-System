from src.tools.tools import web_search,scrape_url

result = scrape_url.invoke({
    "url": "https://timesofindia.indiatimes.com/us" })

print(result)