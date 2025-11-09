## Specter - 100 points
# category => Steganography

---

At the end of the audio there was some unintelligible words; I recognized that pattern from previous CTF challenges. I opened Sonic Visualiser(commonly used in spectogram viewer) and opened my audio.

`Pane->Add Spectrogram->` and there were two options named suggestive for the challenge "CSCTF".
I selected the first option and there was the flag at the end of the .wav file:

![flag.png](img/flag.png)