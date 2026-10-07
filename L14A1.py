def total_price(priceamount, pricetip):
    totalam = priceamount+priceamount*pricetip / 100
    totalam = round(totalam, 2)
    print(totalam)

total_price(1000,67.6767)
