#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('slider')
data = {"slider":s1}
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
<form action = "/cgi-bin/stepper_control.py" method = "POST">
  <input type ="range" name = "slider" min = "0" max="360" value="0"><br>
  <input type="submit" value = "Submit angle"><br><br>
</form>
</div>
</body>
</html>
""")