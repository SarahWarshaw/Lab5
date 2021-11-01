#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('slider')
s2 = data.getvalue('Buttons')
data = {"slider":s1, "Buttons":s2}
with open('stepper_control.txt','w') as f:
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
<form action = "/cgi-bin/stepper_control.py" method = "POST">
""")
print('<input type ="range" name = "slider" min = "0" max="360" value="%s"><br>' % s2)
print("""
  <input type="submit" name = "Buttons" value = "Change Angle">
</form>
</div>
</body>
</html>
""")