from zillow_scrape import ScrapeSF

my_scrape = ScrapeSF()
urls = my_scrape.scrape_urls()
my_print = my_scrape.display_results()
my_print
