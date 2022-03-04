# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()
  
#setting speed rate
engine.setProperty("rate", 170)
#setting voive
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Creating Recogniser() class object
recog1 = spr.Recognizer()

# Creating microphone instance
mc = spr.Microphone()

#printing supported languages

print(

{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'})
# define variables
s = "these are the languages supported , just enter its code when you are promted"

engine.say("These are the supported languages , enter its code while you are prompted")
engine.runAndWait()
# Capture Voice
with mc as source:
	print("Speak 'hello' to initiate the Translation !")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	recog1.adjust_for_ambient_noise(source, duration=0.2)
	audio = recog1.listen(source)
	MyText = recog1.recognize_google(audio)
	MyText = MyText.lower()

# Here initialising the recorder with
# hello, whatever after that hello it
# will recognise it.
if 'hello' in MyText:
	
	# Translator method for translation
	translator = Translator()
	
	# short form of english in which
	# you will speak
	from_lang = str(input("enter a language code that you are going to speak :"))
	
	# In which we want to convert, short
	# form of hindi
	to_lang = str(input("enter a language code that you want to translate :"))
	
	with mc as source:
		
		print("Speak a stentence...")
		recog1.adjust_for_ambient_noise(source, duration=0.2)
		
		# Storing the speech into audio variable
		audio = recog1.listen(source)
		
		# Using recognize.google() method to
		# convert audio into text
		get_sentence = recog1.recognize_google(audio)

		# Using try and except block to improve
		# its efficiency.
		try:
			
			# Printing Speech which need to
			# be translated.
			print("Phase to be Translated :"+ get_sentence)

			# Using translate() method which requires
			# three arguments, 1st the sentence which
			# needs to be translated 2nd source language
			# and 3rd to which we need to translate in
			text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
			
			# Storing the translated text in text
			# variable
			text = text_to_translate.text

			# Using Google-Text-to-Speech ie, gTTS() method
			# to speak the translated text into the
			# destination language which is stored in to_lang.
			# Also, we have given 3rd argument as False because
			# by default it speaks very slowly
			speak = gTTS(text=text, lang=to_lang, slow= False)

			# Using save() method to save the translated
			# speech in capture_voice.mp3
			speak.save("captured_voice.mp3")	
			
			# Using OS module to run the translated voice.
			os.system("start captured_voice.mp3")

		# Here we are using except block for UnknownValue
		# and Request Error and printing the same to
		# provide better service to the user.
		except spr.UnknownValueError:
			print("Unable to Understand the Input")
			
		except spr.RequestError as e:
			print("Unable to provide Required Output".format(e))
