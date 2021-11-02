#!/usr/bin/python37all
import cgi
import json
from urllib.request import urlopen
from urllib.parse import urlencode
import random, time

api = "3UQYF5FIM794CZYD"   # Enter your API key

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('slider')
s2 = data.getvalue('Buttons')
data = {'slider':s1, 'Buttons':s2}
with open('stepper_control.txt','w') as f:
  json.dump(data,f)

params = {
    "api_key":api,
    1: s1}
params = urlencode(params)   # put dict data into a GET string

print("""
<html>
<head>
</head>
<body>
<div style="width:600px;background:#71F282;border:1px;text-align:center">
<br>
<h1>Change Angle or Zero the Motor</h1>
<font size="3" color = "black" face = "helvetica">
<br>
""")

print("""
<form action = "/cgi-bin/stepper_control.py" method = "POST">
""")
print('<input type ="range" name = "slider" min = "0" max="360" value="0"><br>')
print("""
  <input type="submit" name = "Buttons" value = "Change Angle">
  <input type="submit" name ="Buttons" value = "Zero Motor">
</form>
</div>
</body>
</html>
""")

# add "?" to URL and append with parameters in GET string:
url = "https://api.thingspeak.com/update?" + params
try:
    response = urlopen(url)      # open the URL to send the request
    print(response.status, response.reason)  # display the response
    print(response.read()) # display response page data
    time.sleep(16)    # 15 sec minimum
except Exception as e:
    print(e)
