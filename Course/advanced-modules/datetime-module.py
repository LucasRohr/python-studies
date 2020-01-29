import datetime

tempo = datetime.time(18, 26, 42)
print(tempo)

now = datetime.date.today()
print(now)

print(now.year)

before = now.replace(2008)
print(before)

print(now - before)