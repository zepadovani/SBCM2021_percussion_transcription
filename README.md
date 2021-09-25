# SBCM2021_percussion_transcription

DISCLAIMER: Things here are not organized!

Code to quantize and transcribe onset/duration data to a percussion ensemble.
The process is a tecnomorphic adaptation of concatenative synthesis: a target sound and a corpus of percussion sounds were analyzed previously to detect which of the percussion sounds could better substitute the attack (transient portion of detected onsets) and the
decay/sustain/release.
This data (in a csv 'dadosParaNotacao_REVISADO.csv') is used here to generate a percussion score using abjad+abjadext.nauert+LilyPond.

Quantization with 32ths is used here only to show the approximate position of the attacks. Dynamics are not yet transcribed and a more performer-friendly score is not yet generated.

paper authors:
- José Henrique Padovani
- Júlio Guatimosim
- Carlos Guatimosim
