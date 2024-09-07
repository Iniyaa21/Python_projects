import sounddevice as sd
from scipy.io.wavfile import write

sampling_frequency = 44100
duration = 5


recording = sd.rec(int(duration * sampling_frequency),
                   samplerate=sampling_frequency, channels=2)
print("Recording.....")
sd.wait()
print("\nDone")

write("sample.wav", sampling_frequency, recording)
print("\nWritten onto file!")
