from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow
from giris_kayit import Ui_Form as GirisKayitForm
from giris import Ui_Form as GirisForm
from kayit import Ui_Form as KayitForm
from hava_durumu import Ui_MainWindow as HavaDurumuForm
import sys
from pymongo import MongoClient
import requests
from PyQt5.QtCore import Qt


client = MongoClient("mongodb://localhost:27017/")
db = client["kullanici_veritabani"]
kullanici_collection = db["kullanicilar"]

API_KEY = "f0aebc0d6d02f8fe0b0af7974f262bbf"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class GirisKayitWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = GirisKayitForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:/Users/Feyza Nur/Desktop/görselprogramlama/projePyQt5/gunes.png"))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)


        self.ui.pushButton_giris.clicked.connect(self.open_giris)
        self.ui.pushButton_kayit.clicked.connect(self.open_kayit)

    def open_giris(self):
        self.giris_window = GirisWindow()
        self.giris_window.show()
        self.close()

    def open_kayit(self):
        self.kayit_window = KayitWindow()
        self.kayit_window.show()
        self.close()

class GirisWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = GirisForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:/Users/Feyza Nur/Desktop/görselprogramlama/projePyQt5/gunes.png"))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.ui.pushButton_icgiris.clicked.connect(self.login)

    def login(self):
        username = self.ui.lineEdit_kullanici_adi.text()
        password = self.ui.lineEdit_sifre.text()

        user = kullanici_collection.find_one({"kullanici_adi": username, "sifre": password})
        if user:
            QMessageBox.information(self, "Başarılı", "Giriş başarılı!")
            self.open_weather_window(username)
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")
            self.return_to_giris_kayit()

    def open_weather_window(self, username):
        self.weather_window = HavaDurumuWindow(username)
        self.weather_window.show()
        self.close()

    def return_to_giris_kayit(self):
        self.giris_kayit_window = GirisKayitWindow()
        self.giris_kayit_window.show()
        self.close()

class KayitWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = KayitForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:/Users/Feyza Nur/Desktop/görselprogramlama/projePyQt5/gunes.png"))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.ui.pushButton.clicked.connect(self.register)

    def register(self):
        username = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit.text()

        if username and password:
            if kullanici_collection.find_one({"kullanici_adi": username}):
                QMessageBox.warning(self, "Hata", "Bu kullanıcı başkası tarafından kullanılıyor. Yeni bir ad belirleyin.")
                self.return_to_giris_kayit()
            else:
                kullanici_collection.insert_one({"kullanici_adi": username, "sifre": password})
                QMessageBox.information(self, "Başarılı", "Kayıt başarılı!")
                self.open_weather_window(username)
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve şifre boş olamaz!")
            self.return_to_giris_kayit()

    def open_weather_window(self, username):
        self.weather_window = HavaDurumuWindow(username)
        self.weather_window.show()
        self.close()

    def return_to_giris_kayit(self):
        self.giris_kayit_window = GirisKayitWindow()
        self.giris_kayit_window.show()
        self.close()

class HavaDurumuWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.ui = HavaDurumuForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:/Users/Feyza Nur/Desktop/görselprogramlama/projePyQt5/gunes.png"))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.username = username
        self.ui.welcomeLabel.setText(f"Merhaba {username}")

        self.ui.showWeatherBtn.clicked.connect(self.show_weather)
        self.ui.addFavoriteBtn.clicked.connect(self.add_favorite)
        self.ui.removeFavoriteBtn.clicked.connect(self.remove_favorite)
        self.ui.favoriteWeatherBtn.clicked.connect(self.show_favorite_weather)

    def show_weather(self):
        city = self.ui.cityInput.text()
        if city:
            try:
                response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric", "lang": "tr"})
                data = response.json()

                if response.status_code == 200:
                    temp = data["main"]["temp"]
                    weather = data["weather"][0]["description"]
                    self.ui.weatherLabel.setText(f"{city.capitalize()}:\nSıcaklık: {temp}°C\nDurum: {weather.capitalize()}")
                else:
                    QMessageBox.warning(self, "Hata", "Şehir bulunamadı!")
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Hava durumu alınamadı: {e}")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen bir şehir adı girin!")

    def add_favorite(self):
        city = self.ui.cityInput.text()
        if city:
            kullanici_collection.update_one(
                {"kullanici_adi": self.username},
                {"$push": {"favori_sehirler": city}},
                upsert=True
            )
            QMessageBox.information(self, "Başarılı", f"{city} favorilere eklendi!")

    def remove_favorite(self):
        city = self.ui.cityInput.text()
        if city:
            kullanici_collection.update_one(
                {"kullanici_adi": self.username},
                {"$pull": {"favori_sehirler": city}}
            )
            QMessageBox.information(self, "Başarılı", f"{city} favorilerden çıkarıldı!")

    def show_favorite_weather(self):
        user = kullanici_collection.find_one({"kullanici_adi": self.username})
        if user and "favori_sehirler" in user:
            favorite_cities = user["favori_sehirler"]
            weather_info = []
            for city in favorite_cities:
                try:
                    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric", "lang": "tr"})
                    data = response.json()
                    if response.status_code == 200:
                        temp = data["main"]["temp"]
                        weather = data["weather"][0]["description"]
                        weather_info.append(f"{city.capitalize()}: {temp}°C, {weather.capitalize()}")
                    else:
                        weather_info.append(f"{city.capitalize()}: Bilgi alınamadı")
                except Exception as e:
                    weather_info.append(f"{city.capitalize()}: Hata ({e})")
            self.ui.weatherLabel.setText("\n".join(weather_info))
        else:
            QMessageBox.warning(self, "Hata", "Hiç favori şehir eklenmemiş!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = GirisKayitWindow()
    main_window.show()
    sys.exit(app.exec_())
