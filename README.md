# LoveTap (HackUSU Entry)
Connor Meads @Septimis

Benjamin Meads @Benjameads
## Description
In order to prevent hauling around a guest book obtained at your wedding for the rest of your life, we have gutted an analog phone from 1938 into a "voicemail" alternative.  Now guests can simply pick up the receiver and leave a heartfelt message for the lucky couple.  We have implemented a Respberry Pi to listen for when the receiver is lifted via a button in GPIO and begin recording the patrons message.  A red LED light is lit when recording is active for convenience using the same Raspberry Pi GPIO input.  Finally, the message is concluded when the receiver is placed back down and the message is saved locally onto the raspberry pi.

## Libraries
[pyaudio](https://pypi.org/project/PyAudio/) - This library was used in order to gain input from a microphone plugged in via USB into the Raspberry Pi.

[wave](https://docs.python.org/3/library/wave.html) - This library is used as an interface with the .WAV sound format.

[time](https://docs.python.org/3/library/time.html) - This library is used in order to implement the file naming function which uses the date and time as each file name.

[gpiozero](https://gpiozero.readthedocs.io/en/stable/) - This library was used to implement the GPIO inputs from the Raspberry Pi.  Specifically we used *Button* and *LED*.

## Instructions
The project depends on using the linux based sound architecture [ALSA](https://alsa-project.org/wiki/Main_Page) in order to process audio input.  Once an audio input device is plugged into the device, you can find which port it is plugged into by running `lsusb -t` to list each input.  Find the port which has audio as input (ours was input two).  You must first install the required dependecies by typing `sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev` and then followed by `sudo pip3 install pyaudio`.  Be sure to set the 'dev_index' variable within the code to the index of your audio input.

## Works Cited
Our `recordMessage()` function was copied from https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone which was a huge help and guidance.  The only change to this function made by us was making an audio recording record indefinetly until a button was pressed instead of a fixed amount of time.

## Reach Goals
We attempted to upload all audio files created to a database in order for a user to gain easier access to their audio files.  While implementing this, we were saving the audio recording as a `varbinary(MAX)`.  We realized too late that this had massive scaling problems, and we decided to delay this feature until a future date.