from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=FB&d=4&e=6&f=2016&g=d&a=4&b=18&c=2012&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)