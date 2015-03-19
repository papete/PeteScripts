import requests
# import pandas as pd 
import json
import prettytable
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['SMS08000000000000001','LNS14000000'],"startyear":"2011", "endyear":"2014"})
p = requests.post('http://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["Series ID"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes=""
       for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
        if 'M01' <= period <= 'M12':
            if period == "M12":
               month = "December"
            if period == "M11":
               month = "November"
            if period == "M10":
               month = "October"
            if period == "M09":
               month = "September"
            if period == "M08":
               month = "August"
            if period == "M07":
               month = "July"
            if period == "M06":
               month = "June"
            if period == "M05":
               month= "May"
            if period == "M04":
               month = "April"
            if period == "M03":
               month = "March"
            if period == "M02":
               month = "February"
            if period == "M01":
               month = "January"
        x.add_column([seriesId,year,period, value])
    print x.get_string()
    output = open(seriesId + '.txt','w')
    output.write (x.get_string())
    output.close()