import librosa
import numpy as np

def detect_pitch(file_path):
    y, sr = librosa.load(file_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    pitch_values = []
    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        pitch = pitches[index, i]
        if pitch > 0:
            pitch_values.append(pitch)

    if not pitch_values:
        return []
    
    # ピッチから音名への変換
    def hz_to_note(hz):
        note_number = 12 * np.log2(hz / 440.0) + 69
        midi_note = int(round(note_number))

        return librosa.midi_to_note(midi_note)
    
    notes = [hz_to_note(p) for p in pitch_values]

    return notes