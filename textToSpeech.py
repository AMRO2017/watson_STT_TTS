# url and apikey for authentication
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/fadaf24b-8b50-4d18-ac97-8c9e66a4a145'
apikey = '-pvIydEjyPSdd8Y1DSXDHPi5KQCf7R6LtKo4-Td9jYff'

from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# setup service
authenticator = IAMAuthenticator(apikey)
# text to speech service
tts = TextToSpeechV1(authenticator=authenticator)
# set service url
tts.set_service_url(url)

# load the text file
with open('inputSpeech.txt', 'r') as f:
  text = f.readlines()

# make it one block by removing the new lines
text = [line.replace('\n', '') for line in text]
text = ''.join(str(line) for line in text)

# convert a string
with open('outputSpeech.mp3', 'wb') as audioFile:
  receive = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
  audioFile.write(receive.content)
  audioFile.close  

from audioplayer import AudioPlayer

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
AudioPlayer("outputSpeech.mp3").play(block=True)
