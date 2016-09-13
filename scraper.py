from dc_base_scrapers.geojson_scraper import GeoJsonScraper


districts_url = "http://inspire.sthelens.gov.uk/geoserver/ows?service=WFS&version=1.3.0&request=GetFeature&typeNames=INSPIRE%3Apolling_districts&outputFormat=json"
council_id = 'E08000013'


districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
