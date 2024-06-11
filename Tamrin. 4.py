import re

times  = """1:00 am you go and i go at 1:00 pm . 01:00 am may not be ok,
i go at 01:00 pm you can go 1:00am or 1:00pm and 01:00pm is aswell ok,01:00pm also."""

tim = re.findall("[0-1]?[0-9]:[0-5][0-9]\s*[ap]m",text)
print("These are the time you need!" ,tim)
print("\n---------------------------------------------------------------------\n")


urls = """https://www.google.com  https://www.google.com/  http://www.google.com/  http://www.google.com/ 
https://www.google.com/index.html  http://www.google.com/index.html https://google.com  """

url = re.findall("(?:https?://)(?:www.google)(?:|google).com/?(?:index.html)?",tt)
print("These are the URLS you have searched for!",url)
print("\n---------------------------------------------------------------------\n")

dates = """01.01.2023
01/01/23
01-01-23
01.01.23
01/01/2019
01-01-2019
01.01.2019
01/01/19
01-01-19
01.01.19
01/01/2023
01-01-2023
01.01.2023
01/01/23
01-01-23
01.01.23
01/01/2019"""

dt = re.findall("[0-3][0-9][/.-][0-1][0-2][/.-][0-9]?[0-9]?[0-9][0-9]",dates)
print("The dates you want!",dt)

print("\n---------------------------------------------------------------------\n")
