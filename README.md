🧠 Tusk A.I – Voice Controlled Personal Assistant

Tusk A.I is a Python-based voice-controlled personal assistant that listens to user commands and performs tasks such as opening websites, playing music, telling the time, and handling basic interactions.

 Features

 Voice Recognition – Uses Google Speech Recognition API to understand spoken commands.

 Open Websites – Quickly open popular websites like YouTube, Google, Wikipedia, Instagram, X (Twitter), and Spotify via voice command.

 Music Playback – Play local music files using simple voice prompts.

 Time Reporting – Get the current system time on request.

 Basic Chat Handling – Simple response loop for continued interactions.

 Exit Anytime – Quit the assistant with a single command.

🛠 Tech Stack

Language: Python

Libraries Used:

speech_recognition – for voice input

webbrowser – to open websites

os – to handle local file execution

datetime – to provide system time


⚡ Installation & Setup

 Install dependencies:

pip install speechrecognition
pip install pyaudio


Run the assistant:

python main.py

 Example Voice Commands

"Open YouTube" → Opens YouTube in browser

"Open Wikipedia" → Opens Wikipedia

"Open Google" → Opens Google

"Open Instagram" → Opens Instagram

"Open Spotify" → Opens Spotify

"Open music" → Plays a local music file

"What’s the time" → Tells the current time

"Quit" → Exits the program
