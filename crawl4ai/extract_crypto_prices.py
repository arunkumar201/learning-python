import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def extract_data(url, schema, wait_for_selector=None):
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    # Set up crawler config
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=extraction_strategy,
        wait_for=f"css:{wait_for_selector}" if wait_for_selector else None,
    )

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            config=config
        )

        # Handle failure in crawl
        if not result.success:
            print("Crawl failed:", result.error_message)
            return None

        # Parse the extracted JSON data
        data = json.loads(result.extracted_content)
        return data

async def main():
    # Example usage for crypto prices
    crypto_schema = {
        "name": "Crypto Prices",
        "baseSelector": "tr.cds-tableRow-trq0d55",
        "fields": [
            {
                "name": "coin_name",
                "selector": "td.cds-tableCell-tvfsk4v div.cds-flex-f1tjavv3 p.cds-headline-h4steop",
                "type": "text"
            },
            {
                "name": "coin_symbol",
                "selector": "td.cds-tableCell-tvfsk4v div.cds-flex-f1tjavv3 p.cds-label2-l1sm09ec",
                "type": "text"
            },
            {
                "name": "price",
                "selector": "td.cds-tableCell-tvfsk4v div.cds-flex-f1tjavv3 div.cds-flex-f1tjavv3 div",
                "type": "text"
            },
            {
                "name": "price_change",
                "selector": "td.cds-tableCell-tvfsk4v div.cds-flex-f1tjavv3 p[class*='cds-body-bwup3gq']",
                "type": "text"
            },
            {
                "name": "chart",
                "selector": "td.cds-tableCell-tvfsk4v div[data-testid='price-chart']",
                "type": "attribute",
                "attribute": "aria-label"
            }
        ]
    }

    crypto_data = await extract_data(
        url="https://www.coinbase.com/explore",
        schema=crypto_schema,
        wait_for_selector=".cds-tableRow-trq0d55"
    )

    if crypto_data:
        print(f"Extracted {len(crypto_data)} coin entries")
        print(json.dumps(crypto_data, indent=2))

# Run the main function
asyncio.run(main())

# Run the main function
asyncio.run(main())
