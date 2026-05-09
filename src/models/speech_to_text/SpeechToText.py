import speech_recognition as sr
import pyttsx3

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def adjust_to_background_noise(self):
        try:
            with sr.Microphone() as micSource:
                self.recognizer.adjust_for_ambient_noise(micSource, duration=2)
        except Exception as e:
            print(f"Microphone calibration failed: {e}")

    def record_text(self):
        try:
            with sr.Microphone() as micSource:
                self.adjust_to_background_noise()
                audio = self.recognizer.listen(micSource, timeout=1, phrase_time_limit=120)
                text = self.recognizer.recognize_google(audio)
                return text
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
        return ""

    def transcribe_audio_bytes(
        self,
        audio_bytes: bytes,
        sample_rate: int = 16000,
        sample_width: int = 2,
    ) -> str:
        """
        Transcribe raw PCM bytes received from websocket chunks.
        """
        if not audio_bytes:
            return ""
        try:
            audio_data = sr.AudioData(audio_bytes, sample_rate, sample_width)
            return self.recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
            return ""

    def start_listening(self):
        while True:
            text = self.record_text()
            if text:
                print(text)
    

#Testing
if __name__ == "__main__":
    app = SpeechToText()
    app.start_listening()