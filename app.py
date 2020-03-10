from flask import Flask, render_template
import json
import urllib.request
import urllib.parse
import ssl


app = Flask(__name__)


@app.route('/')
def GetMaskInfo():
    lat = #insert_your_lat
    lng = #insert_your_lng
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat={0}&lng={1}&m=5000".format(lat, lng)
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        urlOpen = urllib.request.urlopen(url)
        infoJSON = json.loads(urlOpen.read().decode('utf-8'))
        print(infoJSON)
        a = infoJSON
        a = a['stores']
    except Exception as ee:
        print(ee)
        a = "Asf"
    return render_template("index.html", tem=a)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
