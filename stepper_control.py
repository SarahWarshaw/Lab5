#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('slider')
s2 = data.getValue('button')
selection = data.getValue("submit")
data = {"slider":s1, "button":s2,"chosen":selection}
with open('stepper_control.txt','w') as f:
  json.dump(data,f)

print("""
<html>
<head>
</head>
<body>
<div style="width:600px;background:#71F282;border:1px;text-align:center">
<h1>Choose an angle or zero the motor</h1>
<br>
<font size="3" color = "black" face = "helvetica">
<br>
<form action = "/cgi-bin/stepper_control.py" method = "POST">
  <input type ="range" name = "slider" min = "0" max="360" value="0"><br>
  <input type="submit" name="submit" value = "Submit angle"><br><br>
  <input type = "hidden" name = "button" value = "400">
  <input type="submit" name = "submit" value = "Zero the motor">
</form>
</div>
</body>
</html>
""")