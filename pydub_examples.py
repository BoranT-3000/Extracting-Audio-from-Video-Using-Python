############################################################################################
!pip install pydub
# https://github.com/jiaaro/pydub
############################################################################################


# Arka plan ses ekleme
from pydub import AudioSegment

# İlk ses dosyasını yükleyin
background_music = AudioSegment.from_file("/content/audio_name_one.wav")

# İkinci ses dosyasını yükleyin
voice_over = AudioSegment.from_file("/content/audio_name_two.mp3")

# Arka plan müziği ile ses dosyasını birleştirin
final_audio = background_music.overlay(voice_over, position=0)

# Birleştirilmiş ses dosyasını kaydedin
output_path = "/content/final_audio.mp3"
final_audio.export(output_path, format='mp3')
print(f"Birleştirilmiş ses dosyası '{output_path}' dosyasına başarıyla kaydedildi!")


############################################################################################


from pydub import AudioSegment
import IPython.display as ipd

# İlk ses dosyasını yükleyin
sound1 = AudioSegment.from_file("/content/audio_name_one.wav")

# Ses dosyasının süresini alın
duration_audio_clip = len(sound1)

# İkinci ses dosyasını yükleyin
sound2 = AudioSegment.from_file("/content/audio_name_two.mp3")

# İkinci ses dosyasını, ilk ses dosyasının süresiyle eşleştirmek için kırpın
sound2_clipped = sound2[:duration_audio_clip]

# Arka plan sesinin ses seviyesini azaltın
sound2_quieter  = sound2_clipped - 10

# İki ses dosyasını birleştirin
combined = sound1.overlay(sound2_quieter)

# Birleştirilmiş ses dosyasını kaydedin
output_path = "/content/combined.mp3"
combined.export(output_path, format='mp3')
print(f"Birleştirilmiş ses dosyası '{output_path}' dosyasına başarıyla kaydedildi!")

# Ses dosyasını dinleyebilirsiniz
ipd.Audio(output_path)

############################################################################################

from pydub import AudioSegment

def extract_audio_pydub(video_file: str, output_file: str):
    try:
        # Video dosyasını yükleyin ve sesi videodan çıkarın
        audio = AudioSegment.from_file(video_file, format="mp4")
        # Ses dosyasını kaydedin
        audio.export(output_file, format="mp3")
        print(f"Audio extracted and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Örnek kullanımımız
extract_audio_pydub("/content/video_name.mp4", "/content/audio_name.mp3")

import IPython.display as ipd
ipd.Audio("/content/audio_name.mp3")

############################################################################################

from pydub import AudioSegment

video_file_path = "/content/video_name.mp4"
audio_file_path = "/content/audio_name.mp3"

try:
  audio = AudioSegment.from_file(audio_file_path, format="mp4")
  print(f"Audio file '{audio_file_path}' loaded successfully!")
  audio.export(output_file, format="mp3")
  print(f"Audio extracted and saved to {output_file}")
except FileNotFoundError:
  print(f"Error: Audio file '{video_file_path}' not found.")
except Exception as e:
  print(f"An error occurred: {e}")

############################################################################################

from pydub import AudioSegment
from pydub.effects import normalize
import numpy as np

def add_noise(audio_segment, noise_level=0.05):
    samples = np.array(audio_segment.get_array_of_samples())
    noise = np.random.normal(0, noise_level * np.max(samples), samples.shape)
    noisy_samples = samples + noise
    noisy_samples = np.clip(noisy_samples, -2**15, 2**15-1)
    noisy_audio = audio_segment._spawn(noisy_samples.astype(np.int16).tobytes())
    return noisy_audio

audio = AudioSegment.from_file("/content/audio-geeksforgeeks.wav")
noisy_audio = add_noise(audio, noise_level=0.1)
noisy_audio.export("noisy_audio.mp3", format="mp3")
normalized_audio = normalize(noisy_audio)
normalized_audio.export("normalized_audio.mp3", format="mp3")

############################################################################################


from pydub import AudioSegment

wav_file = AudioSegment.from_file(file = "/content/audio_name.mp3",
                                  format = "mp3")

print(f"data type for the file {type(wav_file)}")
print(f"frame rate of song/file {wav_file.frame_rate}")
print(f"channels of file {wav_file.channels}")
print(f"the number of bytes per sample {wav_file.sample_width}")
print(f"Maximum amplitude {wav_file.max}")
print(f"Length of audio file {len(wav_file)}")

'''
We can change the attributes of file by
changeed_audio_segment = audio_segment.set_ATTRIBUTENAME(x)
'''
wav_file_new = wav_file.set_frame_rate(50)
print(wav_file_new.frame_rate)

############################################################################################

import pydub

def get_audio_info(audio_file):
    try:
        # Check if the input is a valid pydub.AudioSegment object
        if not isinstance(audio_file, pydub.AudioSegment):
            raise TypeError("Input must be a pydub.AudioSegment object.")

        print(f"Data type for the file: {type(audio_file)}")
        print(f"Frame rate (samples per second): {audio_file.frame_rate}")
        print(f"Number of channels (mono or stereo): {audio_file.channels}")
        print(f"Number of bytes per sample: {audio_file.sample_width}")
        print(f"Maximum amplitude: {audio_file.max}")

        # Handle potential division by zero for silence
        if audio_file.duration_seconds > 0:
            print(f"Length of audio file (seconds): {len(audio_file) / 1000}")
        else:
            print(f"Length of audio file (seconds): Silence (0 seconds)")

    except (TypeError, Exception) as e:
        print(f"Error getting audio information: {e}")


# Videonun yolunu girin
video_yolu = "/content/video_name.mp4"

try:
    # Videoyu ses dosyasına dönüştürün
    audio = pydub.AudioSegment.from_file(video_yolu)

    get_audio_info(audio)

    # Ses dosyasını kaydedin
    audio.export("ses.mp3",format = "mp3")
    print(f"Ses dosyası '{video_yolu}' başarıyla ses.mp3 adıyla kaydedildi.")

except Exception as e:
    print(f"Ses dosyası kaydedilirken hata oluştu: {e}")


############################################################################################

from pydub import AudioSegment
import IPython.display as ipd

# ses dosyasını yükleyelim
wav_file = AudioSegment.from_file("/content/audio_name.mp3")  # "audio_name.mp3" yerine kendi dosya adınızı yazın

# sesi yükseltelim
louder_wav_file = wav_file + 10
# sesi indirelim
louder_wav_file.export(out_f = "louder_wav_file.mp3",
                       format = "mp3")

############################################################################################

# Gerekli kütüphaneleri ekleyin
from pydub import AudioSegment
from pydub.playback import play

# Birinci ses dosyası
wav_dosya_1 = AudioSegment.from_file("noice.wav")  # "noice.wav" yerine kendi dosya adınızı yazın

# İkinci ses dosyası
wav_dosya_2 = AudioSegment.from_file("Sample.wav")  # "Sample.wav" yerine kendi dosya adınızı yazın

# İki ses dosyasını birleştirme
wav_dosya_3 = wav_dosya_1 + wav_dosya_2  # + operatörü ile birleştirme

# Birleştirilmiş sesi çalma
play(wav_dosya_3)

############################################################################################

# Video klipleri düzenlemek için gereken fonksiyonu dahil edin
from pydub import AudioSegment

# Stereo ses dosyasını yükleyin
audio = AudioSegment.from_file("/content/stereo_audio.mp3")

# Tekli kanallara bölün
mono_channels  = audio.split_to_mono()
print(mono_channels[0].channels)

for idx, channel in enumerate(mono_channels):
  print(f"Channel {idx+1} has {channel.channels} channel(s)")

# (mono channels) Tekli kanalları dışa aktarın
mono_channels[0].export(out_f="channel_1.mp3",format="mp3")
mono_channels[1].export(out_f="channel_2.mp3",format="mp3")

############################################################################################

from pydub import AudioSegment

# Stereo ses dosyasını yükleyin
stereo_audio = AudioSegment.from_file("stereo_audio.mp3", format="mp3")

# Tekli kanallara bölün
left_channel = stereo_audio.split_to_mono()[0]
right_channel = stereo_audio.split_to_mono()[1]

# (mono channels) Tekli kanalları dışa aktarın
left_channel.export("left_channel.mp3", format="mp3")
right_channel.export("right_channel.mp3", format="mp3")

############################################################################################

