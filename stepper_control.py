#!/usr/bin/python37all
import cgi
import json

try:
  print("Content-type: text/html\n\n")
  data = cgi.FieldStorage()
  selection = data.getValue('two_buttons')
  data = {"two_buttons":selection}
  with open('stepper_control.txt','w') as f:
    json.dump(data,f)

except Exception as e: 
  print(e)

print("""
<html>
<head>
</head>
<body>
<div style="width:600px;background:#71F282;border:1px;text-align:center">
<br>
<h1>Choose an angle or zero the motor</h1>
<font size="3" color = "black" face = "helvetica">
<br>
<form action = "stepper_control.py" method = "POST">
  <input type ="range" name = "slider" min = "0" max="360" value="0"><br>
  <input type="submit" name="button" value = "Submit angle"><br><br>
  <input type="submit" name = "button" value = "Zero the motor">
</form>
</div>
</body>
</html>
""")