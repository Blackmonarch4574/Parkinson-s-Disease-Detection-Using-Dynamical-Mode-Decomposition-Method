import os
import librosa
import numpy as np
from pydmd import HODMD
import pandas as pd
from pydmd.plotter import plot_eigs, plot_summary
from pydmd.preprocessing import hankel_preprocessing

# Function to process audio files and extract modes

def process_audio_file(audio_file, label, hodmd, hankel_size):
    # Load audio signal
    audio_signal, _ = librosa.load(audio_file, sr=None)
    # Apply hankel preprocessing
    X = hankel_preprocessing(audio_signal.reshape(1,-1),hankel_size)
          # Fit HODMD model
    hodmd.fit(X)
    # Get modes and flatten them
    modes = hodmd.modes
    flattened_modes = modes.real.flatten()
    # Append label (1 for Parkinson, 0 for non-Parkinson)
    flattened_modes = np.append(flattened_modes, label)
    return X


hodmd = HODMD(svd_rank=4, exact=False, opt=True, d=10)

# Directory containing Parkinson's disease audio files
parkinson_dir = 'dataset/parkinson'

# Directory containing non-Parkinson's disease audio files
non_parkinson_dir = 'dataset/non_parkinson'

# Initialize an empty list to store data
data = []

# Hankel preprocessing parameters
hankel_size = 20  # Adjust this value based on your data and requirements

# Process Parkinson's disease audio files
for file in os.listdir(parkinson_dir):
    print("park "+file)
    audio_file = os.path.join(parkinson_dir, file)

    mode_data = process_audio_file(audio_file, 1, hodmd, hankel_size)
    data.append(mode_data)
    # print("data = ",  data)

# # Process non-Parkinson's disease audio files
for file in os.listdir(non_parkinson_dir):
    print("non_park "+file)
    audio_file = os.path.join(non_parkinson_dir, file)
    mode_data = process_audio_file(audio_file, 0, hodmd, hankel_size)
    data.append(mode_data)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel file
excel_file = "hodmd_dataset_20_.xlsx"
df.to_excel(excel_file, header=False, index=False)

print("DMD Dataset saved to", excel_file)


# audio_file = "dataset/non_parkinson/B1ACNAGRER49F210320170916.wav"