
import numpy as np
import sys
import os
import glob
#######
import librosa
import librosa.display
from matplotlib import pyplot as plt


def Audio_to_png(file_name,
                         folderName,
                         n_mels=64,
                         frames=5,
                         n_fft=1024,
                         hop_length=512,
                         power=2.0
                         ):


    y, sr = librosa.load(file_name)
    S = librosa.feature.melspectrogram(y=y, sr=sr)

    fig, ax = plt.subplots()
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, x_axis='time',
                            y_axis='mel', sr=sr,
                            fmax=8000, ax=ax)

    # ax.axes.get_xaxis().set_visible(False)
    # ax.axes.get_yaxis().set_visible(False)
    # ax.set_frame_on(False)
    # ax.set_xlabel(None)
    # ax.set_ylabel(None)
    pngName = file_name.replace('wav','png')
    pngName = pngName.replace('Audio\\','')

    fig.savefig(folderName +'/' + pngName)



path = "Audio/"

pngFolder ='normals/'
if os.path.isdir(pngFolder) is False:
    os.mkdir(pngFolder)


for filename in glob.glob(os.path.join(path, '*.wav')):
    Audio_to_png(filename , pngFolder)