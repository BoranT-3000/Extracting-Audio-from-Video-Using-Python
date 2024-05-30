# Python kullanarak Video' dan ses çıkarımı
## Extracting-Audio-from-Video-Using-Python


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
1.MoviePy
2.Pydup
3.ffmpeg

```
pip install moviepy
```



## Lisansı

[MIT](https://choosealicense.com/licenses/mit/)
