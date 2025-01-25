import asyncio
from crawl4ai import *
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

run_config = CrawlerRunConfig(
    word_count_threshold=10,        # Minimum words per content block
    exclude_external_links=True,    # Remove external links
    remove_overlay_elements=True,   # Remove popups/modals
    # markdown_generator=DefaultMarkdownGenerator()
    process_iframes=True           # Process iframe content

    
)

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.geeksforgeeks.org/stack-data-structure/?ref=home-articlecards",
            run_config=run_config,
        )
        # print(result.links)
        # print(result.media)     
        # print(result.fit_markdown) 
        # print(result.cleaned_html)
        print(result.html)

if __name__ == "__main__":
    asyncio.run(main())
