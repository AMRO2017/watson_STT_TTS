# *watson SpeechToText/TextToSpeech*
## The fourth task in the IoT and software development department is to create a stt and tts watson services and link it with watson assistant as follow:
- [X] creat a speech to text and text to speech service using python.
- [x] save the input speech as text file and the output as audio file.
- [x] link the input speech with the output speech by repeating the input speech.
- [ ] link stt and tts to watson assistant.
- [ ] reduce the delays between the previous services.

## the marked tasks are accomplished and here is a list of the included files with detailed description of the work. 
|File|Description|
|----|-----------|
|`inputSpeech.txt`|contains the input speech from the user as text to be used in text to speech service|
|`outputSpeech.mp3`|contains the output speech of watson service which plays the 'inputSpeech.txt' file as audio|
|`requirements.txt`|contains requirements that need instalation to setup the watson streaming service for speech to text service|
|`setup.cfg`|contains metadata used in 'transcribe.py' file for speech to text service|
|`speech.cfg`|contains the apikey and region for watson stt service authentication|
|`textToSpeech.py`|used to setup the watson text to speech service and convert the text in 'inputSpeech.txt' to audio file for to be played and saved|
|`transcribe.py`|used to setup the watson streaming, run the stt service, and obtain the transcribed text in live format|
##   
## Notes:
- All files should be placed in the same directory.
- for the tts service to work properly make sure to install audioplayer and ibm_watson using the command 'pip install audioplayer' in the termninal
- transcribe fie is slightly modified.
- some of the source code is taken from github and the license file is provided.
- running 'transcribe.py' file alone is enough. 
