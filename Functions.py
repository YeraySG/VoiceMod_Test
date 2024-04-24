"""
VoiceMod Test
Yeray SG

"""
import numpy as np
import soundfile as sf
import scipy.signal as sp
import matplotlib.pyplot as plt


def cleanAudio (dirtySignal,whiteNoise):
    dirtyData, dirtySamplerate = sf.read(dirtySignal)
    whiteData, whiteSamplerate = sf.read(whiteNoise)

    filteredSignal = dirtyData - whiteData

    filteredSignal = np.flip(filteredSignal)

    cleanSignal = "cleanedSignal.wav"

    sf.write(cleanSignal,filteredSignal,whiteSamplerate)

    return cleanSignal, whiteSamplerate

def plotSpectrum(audio):
    data, sr = sf.read(audio)
    plt.figure
    plt.specgram(data, Fs=sr)
    plt.xlabel('Time (s)')
    plt.ylabel('F (kHz)')
    plt.title('Signal Spectrum')
    plt.colorbar()
    plt.show()
    