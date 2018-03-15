from urllib import request
stock_url="link"
def download_stock_data(csv_url):
    responce=request.urlopen(csv_url)
    csv=responce.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest_url=r'google.csv'
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(list+"\n")
    fx.close()
download_stock_data(stock_url)

