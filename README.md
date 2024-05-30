# Python kullanarak Video' dan ses çıkarımı
## Extracting-Audio-from-Video-Using-Python

Bu readme.md dosyası, MoviePy, PyDub ve ffmpeg kütüphanelerini kullanarak video düzenleme projeleri için bir rehber olarak tasarlanmıştır.
Ek olarak, Bu kütüphaneler videoları kesmek, videodan ses çıkarmak, birleştirmek, ses eklemek, altyazılar eklemek ve daha fazlasını yapmak için kullanılabilir.


Eğer sanal ortam oluşturma kütüphanesini daha öncesinde kurmadıysanız, lütfen aşağıdaki komut ile kurunuz:
```
pip install virtualenv
```

Şimdi sanal ortamı kuralım
```
# Sanal ortam oluşturma
python -m venv audioenv

# Windows İşletim sistmei için sanal ortamın aktifleştirmesi
audioenv\Scripts\activate.bat # cmd.exe üzerinden aktive etmek için
audioenv\Scripts\activate.ps1 # PowerShell üzerinden aktive etmek için

# MacOS ve Linux İşletim sistmei için Sanal ortamın aktifleştirmesi
source audioenv/bin/activate
```

Kullanılacak Kütüphaneler
1. MoviePy
   - Resmi Dokümantasyonu: [MoviePy Dökümantasyonu](https://zulko.github.io/moviepy/).
   -  ``` pip install moviepy ```
2. Pydup
   - Resmi Dokümantasyonu: [Pydub Dökümantasyonu](https://github.com/jiaaro/pydub/blob/master/API.markdown).
   - ``` pip install pydub ```
3. ffmpeg
   - Windows:
     - ffmpeg.org adresinden Windows için derlenmiş sürümü indirin.
     - İndirilen zip dosyasını çıkarın ve bin klasörünün yolunu PATH ortam değişkenine ekleyin.

   - MacOS:
   - ``` brew install ffmpeg ```

   Linux (Debian/Ubuntu):
   ```
   sudo apt update
   sudo apt install ffmpeg
   ```

   Python ile kütüphanesinin kurulumu:
   ``` pip install ffmpeg-python ```



## Lisansı

[MIT](https://choosealicense.com/licenses/mit/)
