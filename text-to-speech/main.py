from gtts import gTTS

text = "Hello rekha how are you did you finish your lunch"

language = 'en'

object = gTTS(text = text,lang=language,slow=False)

object.save("sample.mp3")