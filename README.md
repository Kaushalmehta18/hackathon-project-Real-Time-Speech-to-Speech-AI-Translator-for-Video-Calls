# hackathon-project-Real-Time-Speech-to-Speech-AI-Translator-for-Video-Calls
This project is a real-time speech-to-speech AI translator designed to break language barriers in video calls. Unlike traditional text-based translators, this system allows users to speak in their native language while the AI translates and speaks aloud in real-time


# Real-Time Speech-to-Speech AI Translator for Video Calls

📌**Problem Statements:**

Language barriers make global communication difficult, especially in video calls. Existing solutions like Google Translate provide text-based translations, but they lack real-time speech-to-speech capabilities. This makes it hard for people to communicate naturally in different languages.

📌**Solution Overview:**

This project is a real-time speech-to-speech translator that allows users to speak in English, automatically translates it to Hindi, and then speaks out the translated text. The program integrates computer vision, speech recognition, translation, and text-to-speech technologies to provide a seamless translation experience.


✅**How It Works:**

🔹Opens the camera using OpenCV.

🔹Continuously listens for user speech.

🔹Converts speech to text using Google Speech Recognition.

🔹Translates text into Hindi (or any other language you choose) using Deep Translator.

🔹Converts translated text into speech using Google Text-to-Speech (gTTS).

🔹Speaks out the translated text while keeping the camera running.


✅**Key Technologies Used**

🔹 OpenCV (cv2) → Handles real-time camera feed display.

🔹 SpeechRecognition (sr) → Captures and converts speech to text.

🔹 Deep Translator (GoogleTranslator) → Translates the text to Hindi (or any other language you choose).

🔹 Google Text-to-Speech (gTTS) → Converts translated text to speech.

🔹 Pygame (pygame.mixer) → Plays translated speech audio efficiently.

🔹 Multithreading (threading) → Ensures smooth execution by running speech processing separately from the camera feed.

🔹 File Handling (os, time) → Manages temporary audio files and prevents system slowdowns.


📌**Setup and Installation Guide:**
1. If you don't have python isntalled in your PC, Intsall Python 3.10 or lower version [link](https://www.python.org/downloads/release/python-3100/)
   
2. If you have python isntalled in your PC 

     i. check the version of python:- open command prompt and type `python --version`, it will display the current version you are using 

     ii. if you are using python 3.10+ version, uninstall the python version

      >-> open command prompt and type "where python" it will display path where you have installed the python, copy that path till python for further use 

      >-> Press `win+I` key it will open settings, go to apps, and search for python and click uninstall it

      >-> and to remove all the leftovers, go to the path where you have installed it previously and delete the python folder 
     iii. then reinstall the python 3.10 or lower version form the above link

     iv. after installing python, set environment variable
   
     >-> open command prompt and type `where python`

     >-> it will display the path of python like this "C:\Users\yourname\AppData\Local\Programs\Python\Python310\python.exe" where you have installed it, copy that path up-to
        "C:\Users\yourname\AppData\Local\Programs\Python\Python310"
   
     >-> then type environment variable in your windows search bar, go to advanced, click environment variable which is at the bottom, then in syatem variables double click on path, it will open the new window, click on "new" button which is dispalyed at the top right corner, and then paste the copied path and then click ok and save the changes. or you can visit this link for more guide [link](https://www.youtube.com/watch?v=91SGaK7_eeY)
   
     >-> and then again open command prompt and type `pip` , if its run then skip this part, and if it doesn't run
        type `python -m pip --version` , if this also doesn't run, open command prompt and type `py -m ensurepip --upgrade` it will install the pip in your PC and the after type `python -m pip --version` it displayed the pip version along with its path like this "pip 25.0.1 from                     
        C:\Users\youname\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)" copy this path till Python310 like this 
        "C:\Users\yourname\AppData\Local\Programs\Python\Python310\" , for more guide visit the [link](https://www.youtube.com/watch?v=F-q9ksowFmw)
   
     >-> again type environment variable in window search bar, go to advanced, and then after go to environment variable which is located path the bottom of that window and click it, after that go to User variable and double click on its path and click on new which is located in the top right, and then after add that path which we have          copied earlier "C:\Users\yourname\AppData\Local\Programs\Python\Python310\" and add Scripts and the end of that path to like like this       
        "C:\Users\yourname\AppData\Local\Programs\Python\Python310\Scripts" and then hit ok and save the chnages and close all the wiindows.
        for more guide visit the [link](https://www.youtube.com/watch?v=DHd36WBQeDo)

3. install pyaudio in your PC

   >-> go to this [link](https://pypi.org/project/PyAudio/#files) and download the pyaudio wheel files which is named as "PyAudio-0.2.14-cp310-cp310-win_amd64" for python 3.10

   >-> after downloading navigate to the path where you install the "PyAudio-0.2.14-cp310-cp310-win_amd64.whl" wheel file and then click on the path and type `cmd`

   >-> after that type `pip install PyAudio-0.2.14-cp310-cp310-win_amd64` and for more guide for the [link](https://www.youtube.com/watch?v=gVZZzb_FIXo)

4. Now open the code in Visual Studio Code, open new terminals and install all the dependencies using by this command `pip install opencv-  python SpeechRecognition deep-translator gtts pygame`
