import cv2
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os
import time
import threading

# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize pygame for audio playback
pygame.mixer.init()

# Flag to track when speech is being processed
is_processing_speech = False
running = True  # Flag to keep the program running

def capture_video():
    """ Open the camera and continuously process speech translation in a background thread """
    global running

    cap = cv2.VideoCapture(0)  # Open webcam
    cv2.namedWindow("Real-Time Speech Translator")

    while running:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Display the video feed
        cv2.imshow("Real-Time Speech Translator", frame)

        # Only start a new speech processing thread if it's not already running
        if not is_processing_speech:
            threading.Thread(target=process_speech, daemon=True).start()

        # Detect 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False  # Stop the loop

    cap.release()
    cv2.destroyAllWindows()
    print("Program exited successfully.")

def process_speech():
    """ Capture speech, translate to Hindi, and convert to speech in a separate thread """
    global is_processing_speech
    is_processing_speech = True  # Mark as processing

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Speak now.")

        try:
            audio = recognizer.listen(source, timeout=5)  # Wait for user input
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")

            # Translate text to Hindi
            translated_text = GoogleTranslator(source="auto", target="hi").translate(text)
            print(f"Translated: {translated_text}")

            # Convert translated text to speech
            translated_audio_path = text_to_speech(translated_text, "hi")

            if translated_audio_path:
                play_audio(translated_audio_path)

        except sr.WaitTimeoutError:
            print("No speech detected, waiting again...")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Speech recognition service unavailable.")

    is_processing_speech = False  # Mark as done processing

def text_to_speech(text, language):
    """ Convert text to speech and save as an audio file """
    unique_filename = f"translated_speech_{int(time.time())}.mp3"

    # Save new translated speech
    tts = gTTS(text=text, lang=language)
    tts.save(unique_filename)
    return unique_filename

def play_audio(audio_path):
    """ Play the translated audio in a separate thread to avoid lag """
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # Wait until audio finishes
        time.sleep(0.1)  # Reduce CPU usage

    pygame.mixer.music.stop()  # Stop previous audio
    pygame.mixer.quit()  # Fully unload the audio system
    pygame.mixer.init()  # Reinitialize for next playback

    # Delete the audio file after playing to free memory
    if os.path.exists(audio_path):
        os.remove(audio_path)

if __name__ == "__main__":
    capture_video()
