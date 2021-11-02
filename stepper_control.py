#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('slider')
s2 = data.getvalue('Buttons')
data = {'slider':s1, 'Buttons':s2}
with open('stepper_control.txt','w') as f:
  json.dump(data,f)

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
print('<input type ="range" name = "slider" min = "0" max="360" value="%s"><br>' % s2)
print("""
  <input type="submit" name = "Buttons" value = "Change Angle">
  <input type="submit" name ="Buttons" value = "Zero Motor">
</form>
</div>
</body>
</html>
""")