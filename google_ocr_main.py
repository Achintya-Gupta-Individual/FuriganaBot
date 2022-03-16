import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import io
import os
import pyperclip
# Imports the Google Cloud client library
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\precise-hangar-344222-c8927ba18396.json"
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

def main():
	event_handler = ClipboardEventHandler()
	observer = Observer()
	observer.schedule(event_handler, "C:/Users/achin/AppData/Local/Packages/MicrosoftWindows.Client.CBS_cw5n1h2txyewy/TempState/ScreenClip", recursive=True)  
	observer.start() 
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

class ClipboardEventHandler(FileSystemEventHandler):
	looking = True
	
	def on_created(self, event):
		time.sleep(1)
		if ".png" in event.src_path:
			if self.looking:
				# The name of the image file to annotate
				file_name = os.path.abspath(event.src_path)
				print("the path is {!r}".format(file_name))
				print("path exists: ", os.path.exists(file_name))
				print("it is a file: ", os.path.isfile(file_name))
				print("file size is: ", os.path.getsize(file_name))
				# Loads the image into memory
				with io.open(file_name, 'rb') as image_file:
					content = image_file.read()
				
				image = vision.Image(content=content)

				# Performs label detection on the image file
				response = client.text_detection(image=image, image_context={"language_hints": ["ja"]})
				print(response.full_text_annotation.text)
				pyperclip.copy(response.full_text_annotation.text)

			self.looking = not self.looking
main()