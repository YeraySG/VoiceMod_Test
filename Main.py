"""
VoiceMod Test
Main file
Yeray SG
"""
from Functions import cleanAudio, plotSpectrum
# These paths should be updated before running the code  
challengeAudio = "C:/Users/XXX/Desktop/VoiceModTest/Challenge.wav" 
whiteNoiseAudio = "C:/Users/XXX/Desktop/VoiceModTest/whiteNoiseMono.wav"

decodedSignal = cleanAudio(challengeAudio,whiteNoiseAudio)
plotSpectrum(decodedSignal)