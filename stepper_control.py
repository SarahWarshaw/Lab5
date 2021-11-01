#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('LED')
s2 = data.getvalue('slider')
data = {"LED":s1, "slider":s2}
with open('led_brightness_multiple.txt','w') as f:
  json.dump(data,f)

print("""
<html>
<head>
</head>
<body>
<div style="width:600px;background:#71F282;border:1px;text-align:center">
<br>
<font size="3" color = "black" face = "helvetica">
<br>
""")

if s1 == str(13):
  print('RED LED BRIGHTNESS = %s' %s2) 
elif s1 ==str(19):
  print('WHITE LED BRIGHTNESS = %s' %s2) 
else:
  print('BLUE LED BRIGHTNESS = %s' %s2) 


print("""
<form action = "/cgi-bin/led_brightness.py" method = "POST">
  <input type = "radio" name = "LED" value = "13" checked> LED 1<br>
  <input type = "radio" name = "LED" value = "19"> LED 2<br>
  <input type = "radio" name = "LED" value = "26"> LED 3<br>
""")
print('<input type ="range" name = "slider" min = "0" max="100" value="%s"><br>' % s2)
print("""
  <input type="submit" value = "Change LED brightness">
</form>
</div>
</body>
</html>
""")