import io

text = 'i am a text'

file = io.StringIO(text)

print(file.read())