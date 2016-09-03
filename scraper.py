from geojson_scraper import scrape


districts_url = "http://inspire.sthelens.gov.uk/geoserver/ows?service=WFS&version=1.3.0&request=GetFeature&typeNames=INSPIRE%3Apolling_districts&outputFormat=json"
council_id = 'E08000013'


scrape(districts_url, council_id, 'utf-8', 'districts')
