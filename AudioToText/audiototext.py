import requests
from pydub import AudioSegment
import io
import os

url = input("URL: ")
print("Downloading...")
data = requests.get(url).content
print("Saving...");
open('audio.mp3', 'wb').write(data)
sound = AudioSegment.from_mp3("audio.mp3")
print("Splitting...")
chunks = []
while len(chunks) * 20 < sound.duration_seconds: # wit.ai akzeptiert nur audiodateien, welche unter 20 sekunden lang sind. also splitten wir es einfach in mehrere 19,5s lange audio dateien :)
	buffer = io.BytesIO()
	splitted = sound[(len(chunks) * 20e3):(len(chunks) * 20e3) + 19500]
	splitted.export(buffer, format="mp3")
	chunks.append(buffer.getvalue())
token = ""
with open('token.txt') as file:
	token = file.read()

headers = {'Authorization': 'Bearer '+token,
           'Content-Type': 'audio/mpeg3'
           }
text = ""
for i, chunk in enumerate(chunks):
	print("Uploading to wit.ai.. (%s/%s)" % (i, len(chunks)))
	req = requests.post('https://api.wit.ai/speech?v=20201006', data=chunk, headers=headers)
	try:
		if req.json()["text"]:
			text += req.json()["text"] + "\n"
	except:
		print("Couldn't transcribe chunk %s (second %s to %s)" % (i, i * 20, i * 20 + 20))
		print(req.text)

with open("result.txt", "w") as f:
	f.write(text)

os.system("result.txt &")