from .base import *

USER_AGENT = "City Scrapers [production mode]. Learn more and say hello at cityscrapers.org"

# Configure item pipelines
ITEM_PIPELINES = {
    "city_scrapers_core.pipelines.DefaultValuesPipeline": 100,
    "city_scrapers_core.pipelines.AzureDiffPipeline": 200,
    "city_scrapers_core.pipelines.MeetingPipeline": 300,
    "city_scrapers_core.pipelines.OpenCivicDataPipeline": 400,
}

SENTRY_DSN = os.getenv("SENTRY_DSN")

EXTENSIONS = {
    "city_scrapers_core.extensions.AzureBlobStatusExtension": 100,
    "scrapy_sentry.extensions.Errors": 10,
    "scrapy.extensions.closespider.CloseSpider": None,
}

FEED_EXPORTERS = {
    "json": "scrapy.exporters.JsonItemExporter",
    "jsonlines": "scrapy.exporters.JsonLinesItemExporter",
}

FEED_FORMAT = "jsonlines"

FEED_STORAGES = {
    "azure": "city_scrapers_core.extensions.AzureBlobFeedStorage",
}

AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")
CITY_SCRAPERS_STATUS_CONTAINER = os.getenv("AZURE_STATUS_CONTAINER")

FEED_URI = (
    "azure://{account_name}:{account_key}@{container}"
    "/%(year)s/%(month)s/%(day)s/%(hour_min)s/%(name)s.json"
).format(
    account_name=AZURE_ACCOUNT_NAME,
    account_key=AZURE_ACCOUNT_KEY,
    container=AZURE_CONTAINER,
)

FEED_PREFIX = "%Y/%m/%d"

if os.getenv("WAYBACK_ENABLED"):
    SPIDER_MIDDLEWARES = {
        **SPIDER_MIDDLEWARES,
        "city_scrapers.middleware.CityScrapersWaybackMiddleware": 500,
    }
