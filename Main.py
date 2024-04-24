"""
VoiceMod Test
Main file
Yeray SG
"""
from Functions import cleanAudio, plotSpectrum

challengeAudio = "C:/Users/Yeray/Desktop/VoiceModTest/Challenge.wav"
whiteNoiseAudio = "C:/Users/Yeray/Desktop/VoiceModTest/whiteNoiseMono.wav"

decodedSignal = cleanAudio(challengeAudio,whiteNoiseAudio)
plotSpectrum(decodedSignal)