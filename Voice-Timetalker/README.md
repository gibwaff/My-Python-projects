### README

# Voice Recognition and Speech Synthesis Application

This application is a simple Python-based program that uses the Vosk library for speech recognition and the pyttsx4 library for text-to-speech synthesis. It continuously listens for spoken commands and can respond with the current time when the command "time" is detected.

---

## Features

1. **Real-time Speech Recognition**: 
   - Listens to audio input through a microphone.
   - Converts spoken words into text using the Vosk model.

2. **Text-to-Speech Response**:
   - Uses `pyttsx4` to convert text into spoken output.
   - Responds with the current time when the word "time" is detected.

3. **Customizable**:
   - Can be expanded to recognize additional commands and perform corresponding actions.

---

## Prerequisites

### Python Libraries
Make sure the following libraries are installed:
- `vosk`: For speech recognition.
- `pyaudio`: To capture audio from the microphone.
- `pyttsx4`: For text-to-speech synthesis.
- `json`: Built-in library for parsing recognition results.
- `datetime`: Built-in library for fetching the current time.

Install the necessary packages using `pip`:
```bash
pip install vosk pyaudio pyttsx4
```

### Vosk Model
Download a compatible Vosk model from the [Vosk Models page](https://alphacephei.com/vosk/models). Extract the model files and ensure the directory is named `model` in the same directory as the script.

---

## Usage

1. **Setup**:
   - Ensure a microphone is connected to your system.
   - Place the downloaded Vosk model in a folder named `model` within the same directory as the script.

2. **Run the Script**:
   Execute the script:
   ```bash
   python script_name.py
   ```

3. **Speak Commands**:
   - Say "time" into the microphone.
   - The program will respond with the current time in both text and speech.

---

## Code Overview

1. **Speech Recognition**:
   - The `KaldiRecognizer` from the `vosk` library processes live audio input to recognize speech.

2. **Speech Synthesis**:
   - The `pyttsx4` library converts recognized text into speech for auditory responses.

3. **Command Handling**:
   - Recognizes the keyword `time` and provides the current time as a response.

---

## Example Interaction

1. Run the script:
   ```
   python script_name.py
   ```

2. Speak into the microphone:
   ```
   User: time
   ```

3. Program responds:
   ```
   Console: "Сейчас 14:35"
   Audio: "Сейчас 14:35"
   ```

---

## Troubleshooting

- **No Audio Input**:
  Ensure the microphone is connected and accessible. Check system permissions for audio input.

- **Model Not Found**:
  Ensure the `model` directory exists in the same directory as the script and contains the Vosk model files.

- **Dependencies Missing**:
  Install required libraries using `pip`.

---

## Future Enhancements

1. Add support for additional commands.
2. Improve the program's ability to handle continuous and natural speech.
3. Provide support for multiple languages with appropriate models.

--- 

Enjoy using the application!
