#library and modules used
import requests

import configparser
from flask import Flask,render_template,request

# make the appp
app=Flask(__name__)
#landing page
@app.route('/')
#function for index page
def weather_dashboard():
    return render_template('index.html')
'''
now we have to make a post request to get the zip code from index
I have to go to the result page, fetch the API and see the result

POST request is when you send the data into some web services or kind of
end point
'''

#declarative
#result page
@app.route('/results',methods=['POST'])
#result page function
def results():

    zip_code=request.form['zipcode']
    api_key=get_apikey()
    data=get_weather_result(zip_code,api_key)
    #variables we need in json

    temp='{0:.2f}'.format(data['main']['temp'])
    feels_like='{0:.2f}'.format(data['main']['feels_like'])
    weather_des=data['weather'][0]['main']
    location=data['name']

    return render_template('results.html',location=location,temp=temp,weather=weather_des,feels_like=feels_like)

def get_apikey():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweatherapi']['api']

def get_weather_result(zip_code,api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code,api_key)
    r=requests.get(api_url)
    return r.json()
    #print(api_url)




#driver code
if __name__=='__main__':
    app.run()






