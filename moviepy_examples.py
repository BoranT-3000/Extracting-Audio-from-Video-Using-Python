

# Commented out IPython magic to ensure Python compatibility.
# Moviepy examples
!pip install moviepy

from moviepy.editor import VideoFileClip

# Ses çıkarmak istediğiniz video dosyasının adını ve yolunu belirtin
video_dosya_yolu = "/content/Never Gonna Give You Up.mp4"

# Video dosyasını yükleyin
video_clip = VideoFileClip(video_dosya_yolu)

# Video dosyasından tam bir ses almak için başlangıç ve bitiş sürelerini belirtin
baslangic_zamani = 0  # Başlangıç zamanı (saniye cinsinden)
bitis_zamani = video_clip.duration  # Bitiş zamanı (saniye cinsinden)

# Video dosyasından sesi çıkarın
ses_clip = video_clip.audio.subclip(baslangic_zamani, bitis_zamani)

# Ses dosyasını kaydedin ve kalitesini belirleyin
ses_dosya_yolu = "ses.mp3"
ses_clip.write_audiofile(ses_dosya_yolu, codec='mp3', bitrate='320k')

# Belleği temizleyin ve kaynakları serbest bırakın
video_clip.close()
ses_clip.close()




from moviepy.editor import VideoFileClip
import os

# Define the input video file and output audio file
video_file = "/content/geeksforgeeks.mp4"
filename_with_path, ext = os.path.splitext(video_file)
filename = os.path.basename(filename_with_path)  # Sadece dosya adını alır (yol olmadan)
output_file = f"{filename}.mp3"
print(f"Filename without extension: {output_file}")

try:
  video_clip = VideoFileClip(video_file)
  audio_clip = video_clip.audio
  audio_clip.write_audiofile(output_file)
except Exception as e:
  print(f"Error extracting audio: {e}")
finally:
    if video_clip:
      video_clip.close()
    if audio_clip:
      audio_clip.close()


print(f"Extracting audio from '{video_file}' to '{output_file}'...")




from moviepy.editor import VideoFileClip
import os

def extract_audio_moviepy(video_file, output_format='mp3')->None:
    try:
        # Dosya adını ve uzantısını ayır
        filename_with_path, _ = os.path.splitext(video_file)
        filename = os.path.basename(filename_with_path)
        output_file = f"{filename}.{output_format}"

        # Video dosyasını yükle
        video_clip = VideoFileClip(video_file)

        # Sesi çıkar
        audio_clip = video_clip.audio

        # Ses dosyasını kaydet
        audio_clip.write_audiofile(output_file)
        print(f"Extracting audio from '{video_file}' to '{output_file}' completed successfully!")

        return output_file
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None
    finally:
        # Kaynakları serbest bırak
        if 'video_clip' in locals():
            video_clip.close()
        if 'audio_clip' in locals():
            audio_clip.close()

# Örnek kullanım
video_path = "/content/geeksforgeeks.mp4"
output_audio = extract_audio_moviepy(video_path, 'mp3')
if output_audio:
    print(f"Audio file saved at: {output_audio}")



# blur video
from scipy.ndimage import gaussian_filter
from moviepy.editor import VideoFileClip
import numpy as np

def blur(image):
    """ Returns a blurred (radius=2 pixels) version of the image """
    return gaussian_filter(image.astype(np.float32), sigma=2)

try:
  clip = VideoFileClip("/content/geeksforgeeks.mp4")
  clip_blurred = clip.fl_image(blur)
  clip_blurred.write_videofile("blurred_video.mp4", fps=clip.fps)
except Exception as e:
  print(f"Error blurring video: {e}")



# blur and create gif file
from scipy.ndimage import gaussian_filter
from moviepy.editor import VideoFileClip, concatenate_videoclips

def blur(image):
    """ Returns a blurred (radius=4 pixels) version of the image """
    return gaussian_filter(image.astype(float), sigma=4)

# Video dosyasının yolunu tanımlayalım
video_path = "/content/video.mp4"
output_path = "/content/blurdemo.gif"

# Videoyu açın ve 480 piksel genişliğe yeniden boyutlandırılmış alt klipler oluşturun
clip1 = VideoFileClip(video_path).subclip(1,2).resize(width=480)
clip2 = VideoFileClip(video_path).subclip(2,4).resize(width=480)
clip3 = VideoFileClip(video_path).subclip(4,6).resize(width=480)

# İkinci klibe bulanıklaştırma efekti uygulayın
clip2_blurred = clip2.fl_image( blur )

# Klipleri birleştirerek son bir video haline getirin
final_clip = concatenate_videoclips([clip1, clip2_blurred, clip3])

# Son videoyu bir GIF dosyasına yazın
final_clip.write_gif(output_path)
print(f"Blurry demo GIF created at {output_path}")


## speech recognition from audio
# %pip install -q moviepy SpeechRecognition
import moviepy.editor as mp
import speech_recognition as sr
import textwrap

# Videoyu yükleyelim
video = mp.VideoFileClip("/content/video_name.mp4")

# videodan sesi çıkartalım
audio_file = video.audio
audio_file.write_audiofile("audio_name.mp3")

# Initialize recognizer
r = sr.Recognizer()

# Ses dosyasını yükleyelim
with sr.AudioFile("audio_name.mp3") as source:
    try:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        # text = r.recognize_google(audio_data, language='tr-TR')
        print("\nVideodan elde edilen metin şöyledir: \n")
        print(textwrap.fill(text, 80))

    except Exception as e:
        print("Ses algılandığında bir hata oluştu:", str(e))



# Video klipleri düzenlemek için gereken her şeyi içe aktarın
from moviepy.editor import VideoFileClip

# Videoyu yükleme
clip = VideoFileClip("/content/video_name.mp4")  # video_adı yerine video dosyanızın adını yazın

# Videodan alt klip alma
sub_clip = clip.subclip(0, 5)  # Başlangıç ve bitiş zamanı (saniye)

# Genişlik, yükseklik, süre ve klibin adını alma
yukseklik = sub_clip.h
genislik = sub_clip.w
ad = sub_clip.filename
clip_suresi = clip.duration
alt_klip_suresi = sub_clip.duration
ses = sub_clip.audio  # Alt klipte ses olup olmadığını kontrol etme

# Klibin başlangıç ve bitiş zamanını alma
baslangic_zamani = clip.start
bitis_zamani = clip.end

# Genişlik, yükseklik, süre ve adın değerlerini yazdırma
print("Dosya Adı     : " + ad)
print("Klip Süresi   : " + str(clip_suresi))
print("Alt Klip Süresi: " + str(alt_klip_suresi))
print("Klibin Genişliği: " + str(genislik))
print("Klibin Yüksekliği: " + str(yukseklik))

print(f"Başlangıç Zamanı: {baslangic_zamani}")
print(f"Bitiş Zamanı   : {bitis_zamani}")

# Klibi kaydetme (şu an için yorum satırı olarak)
# sub_clip.write_videofile("alt_klip.mp4")

# Videoya kenarlık ekleme
sub_clip = sub_clip.margin(40)  # Kenarlık boyutu (piksel)

# Yeni kare hızıyla yeni klip oluşturma
sub_clip = sub_clip.set_fps(5)  # Yeni kare hızı (FPS)

# Renk efekti uygulama
sub_clip = sub_clip.fx(vfx.colorx, 1.5)  # Renk yoğunluğu (1.0 normal)

sub_clip = sub_clip.fx(vfx.mirror_y)  # Videoyu yatay olarak yansıtma

# Verilen klibin yüzeysel kopyasını oluşturma
kopyalanmis_klip = sub_clip.copy()

print("---------------------------------------")
sub_clip.ipython_display(width=480)  # Son klibi göster (genişlik 480 piksel)
# sub_clip.ipython_display(loop=3)  # Videoyu 3 kez döngü (kütüphane gerekli)




## üst üste video oynatmak
from moviepy.editor import VideoFileClip,CompositeVideoClip
import IPython.display as ipd

clip = VideoFileClip("/content/video_name.mp4")
rclip = clip.resize(0.8).without_audio()
comp = CompositeVideoClip([clip, rclip.set_pos('center')])
comp.write_videofile('resize_fname.mp4')



# make clip slower 0.7 and darken the video
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx

clip = VideoFileClip("/content/video_name.mp4")
newClip = clip.fx(vfx.speedx, 0.7).fx(vfx.colorx, 0.8)
newClip.write_videofile('slowerDarker.mp4', codec="libx264", audio_codec="aac")
print("---------------------------------------")
newClip.ipython_display(width = 480)



## resize video
from moviepy.editor import VideoFileClip

def resize_video(input_video_path:str, output_video_path:str, new_width:int=640, new_height:int=360) -> None:
  """Video klibini yeniden boyutlandırıp yeniden boyutlandırılmış versiyonunu kaydeder.

  Args:
      input_video_path (str): Giriş video dosyasının yolu.
      output_video_path (str): Yeniden boyutlandırılmış video dosyasını kaydetmek için yol.
      new_width (int, optional): İstenen genişlik piksel cinsinden. Varsayılan değer 640.
      new_height (int, optional): İstenen yükseklik piksel cinsinden. Varsayılan değer 360.
  """

  try:
      # Video klibini yükleyen kısım
      clip = VideoFileClip(input_video_path)
      duration = clip.duration
      print(duration)
      subclip = clip.subclip(0, float(duration))

      # Video klibini boyutlandıran kısım
      resized_clip = subclip.resize((new_width, new_height))

       # Yeniden boyutlandırılmış video klibini yeni bir dosyaya yazan ksıım
      resized_clip.write_videofile(output_video_path, codec="libx264", fps=clip.fps)
      print(f"Yeniden boyutlandırılmış video '{output_video_path}' olarak kaydedildi.")

  except Exception as e:
      print(f"Video boyutlandırma hatası: {e}")
  finally:
    clip.close()


# Example usage
input_video_path = "/content/geeksforgeeks.mp4"
output_video_path = "output_video_resized.mp4"
resize_video(input_video_path, output_video_path)

