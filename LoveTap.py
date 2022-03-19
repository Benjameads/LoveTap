from blinker import receiver_connected
import pyaudio
import wave
import time
from gpiozero import Button

receiverBtn = Button(2)
#makeFile() code found at https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
def recordMessage():
    audio = pyaudio.PyAudio()

    form_1 = pyaudio.paInt16 #16 bit resolution
    chans = 1 #1 channel
    samp_rate = 44100 #44.1kHz sampling rate
    chunk = 4096 #2^12 samples for buffer
    record_secs = 30 # 30 seconds to record
    dev_index = 2 #device index found by p.get_device_info_by_index(i)

    #build file name based on the time it was recorded
    timeStr = time.strftime("%d%b%Y_%H:%M:%S", time.localtime(time.time())) #ex: 03Aug2021_10:45:08.wav
    wav_output_filename = '{0}.wav'.format(timeStr)

    #create pyaudio stream
    stream = audio.open(format = form_1, rate = samp_rate, channels = chans, input_device_index = dev_index, input = True, frames_per_buffer = chunk)

    print('Starting the recording...')
    frames = []

    #loop through and stream and append audio chunks to frames array 1 second at a time
    while True:
        for i in range(0, int(samp_rate / chunk)):
            data = stream.read(chunk)
            frames.append(data)
        if receiverBtn.is_pressed:
            break
    
    print('Recording finsihed...')

    #close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wavefile = wave.open(wav_output_filename, 'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

if __name__ == "__main__":
    # always be listening to the input
    while True:
        if not receiverBtn.is_pressed:
            recordMessage()
            time.sleep(1)
            print('Recording saved...')
