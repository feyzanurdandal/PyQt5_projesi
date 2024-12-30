# Hava Durumu Uygulaması

## Proje Özeti

Günlük hayatta insanlar pek çok işini hava durumuna göre düzenler. Bu yüzden anlık ve hızlı bir şekilde hava durumu bilgilerini görebilmek yaşamımızı çoğu açıdan kolaylaştıracaktır. Bu projenin amacı, PyQt5 kullanılarak bir hava durumu uygulaması geliştirmek ve MongoDB ile kullanıcı verilerini saklamaktır. Proje, kullanıcıların kayıt olup giriş yapabileceği, hava durumu bilgilerini alabileceği, favori şehirlerini yönetebileceği ve istediğinde hızlıca favori şehirlerinin hava durumunu görebileceği bir arayüz sunar. Proje tamamen Türkçe olup, her yaştan insanın rahatlıkla kullanabileceği şekilde kullanıcı dostu olarak tasarlanmıştır.

## Kullanılan Yöntemler

### Yazılımsal ve Teknik Yöntemler
1. **Programlama Dili**: Python
2. **GUI Kütüphanesi**: PyQt5
3. **Veritabanı**: MongoDB
4. **API**: OpenWeatherMap (Hava durumu verileri için)

### Uygulama Aşamaları

#### 1. GirisKayitWindow
Bu sınıf, kullanıcıların kayıt veya giriş yapması için ana pencereyi temsil eder.
- **pushButton_giris**: Kullanıcının giriş ekranına yönlendirilmesini sağlar.
- **pushButton_kayit**: Kullanıcının kayıt ekranına yönlendirilmesini sağlar.

#### 2. GirisWindow
Bu sınıf, kullanıcıların giriş yapabileceği ekranı temsil eder.
- **login()**: Kullanıcı giriş bilgilerinin MongoDB veritabanında kontrol edilmesini sağlar.
- **open_weather_window()**: Giriş başarılı olduğunda kullanıcıyı hava durumu penceresine yönlendirir.
- **return_to_giris_kayit()**: Hatalı giriş durumunda kullanıcıyı ana sayfaya döndürür.

#### 3. KayitWindow
Bu sınıf, kullanıcıların kayıt olabileceği ekranı temsil eder.
- **register()**: Kullanıcı bilgilerinin MongoDB'ye kaydedilmesini sağlar.
- **open_weather_window()**: Kayıt başarılı olduğunda kullanıcıyı hava durumu penceresine yönlendirir.
- **return_to_giris_kayit()**: Kayıt başarısızlığı durumunda kullanıcıyı ana sayfaya döndürür.

#### 4. HavaDurumuWindow
Bu sınıf, hava durumu bilgilerini ve favori şehirleri yönetmek için kullanılır.
- **show_weather()**: Kullanıcının girdiği şehir için hava durumu verilerini OpenWeatherMap API'dan alır ve ekranda gösterir.
- **add_favorite()**: Kullanıcının favori şehirler listesine yeni bir şehir ekler.
- **remove_favorite()**: Kullanıcının favori şehirler listesinden bir şehri çıkarır.
- **show_favorite_weather()**: Kullanıcının favori şehirleri için hava durumu bilgilerini gösterir.

#### 5. Veritabanı Yapısı
- **Database Adı**: kullanici_veritabani
- **Collection Adı**: kullanicilar

Örnek Veri Yapısı:
```json
{
  "kullanici_adi": "kullanici1",
  "sifre": "12345",
  "favori_sehirler": ["Istanbul", "Ankara"]
}
```
## 6. API Kullanımı

- **API URL**: [OpenWeatherMap API](https://api.openweathermap.org/data/2.5/weather)
- **Parametreler**:
  - `q`: Şehir adı
  - `appid`: API anahtarı
  - `units`: Metrik sistemde sıcaklık birimi
  - `lang`: Dil ayarı (tr)

## Özellikler

- Kullanıcı giriş ve kayıt sistemi
- Gerçek zamanlı hava durumu bilgisi
- Favori şehirler ekleme ve çıkarma
- Favori şehirlerin hava durumu görüntülemesi

## Hata Yönetimi

- Yanlış giriş veya kayıt bilgisi girildiğinde hata mesajı görüntülenir.
- Şehir bilgisi alınamadığında veya API hatası durumunda hata mesajı görüntülenir.





