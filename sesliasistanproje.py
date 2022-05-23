import speech_recognition as sr
import random as rd
import datetime
from translate import Translator
import webbrowser
from gtts import gTTS
from playsound import playsound
import time
import os
import subprocess as sp
import pyautogui
from selenium import webdriver
import sqlite3 as sql
isim = "q"
def veriEkle(arananCumle, link):
    db = sql.connect("C:/Users/Berat Can Kara/Documents/arananlar.db")
    im = db.cursor()
    tabloOlustur = """CREATE TABLE IF NOT EXISTS arananVeriler(cumle,link)"""
    arananlariEkle = """INSERT INTO arananVeriler VALUES({}{})""".format(arananCumle,link)
    im.execute(tabloOlustur)
    im.execute(arananlariEkle)
    db.commit()
    db.close()
while True:
    class verilecekCevaplar:
        kapatcümle = ["kapat", "hoşçakal", "görüşmek üzere", "kendine iyi bak", "görüşürüz"]
        yas = "kaç yaşındasın yaşın kaç ne zamandır bu dünyada varsın yaşın kaç senin kaç yaşındasın sen ya sen kaç yaşındasın"
        yasc = ["birkaç gündür bu dünyada varlığımı sürdürmekteyim.", "birkaç günlüğüm.",
                "şu büyük evrende sadece birkaç gündür elektrik tüketiyorum."]
    nasil = ["İyiyim sen nasılsın?", "İyi gibi...", "Ne iyi ne kötü yuvarlanıyoruz işte."]
    day = Translator(to_lang="Turkish").translate(datetime.datetime.now().strftime("%A"))
    kelimeler = {"bugün hava nasıl":"Bugün hava çok güzel.","saat kaç":datetime.datetime.now().strftime("%H:%M:%S"),
                 "bugün günlerden ne":day,"ne yapıyorsun":"Senin için çalışıyorum.","nerelisin":"Samsunluyum ama İstanbulda yaşıyorum.","nerede yaşıyorsun":"Senin bilgisayarında","neredesin":"Bilgisayarının hafızasında barınıyorum","seni kim yaptı":"beni Berat yaptı ona sonsuz minnettarım","senin yaratıcın kim":"hepimizin yaratıcısı olan yüce Allah.","nerede doğdun":"Beratın bilgisayar masasında bir gece ansızın dünyaya geldim" }
    gereksiz = ["ben kimim","","memorhcccw","ahmet","uyu"]
    hepsi = verilecekCevaplar.kapatcümle+gereksiz+list(verilecekCevaplar.yas)
    r = sr.Recognizer()
    def record():
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio,language="tr-TR")
            except sr.UnknownValueError:
                print("")
            except sr.RequestError:
                speak("Sistem çalışmıyor.")
            return voice
    def response (voice):
        print(voice)
        ses = set(voice.split())
        if voice in " ":
            return voice
        if voice in kelimeler.keys():
            speak(kelimeler[voice])
        elif voice == "ahmet":
            while 1:
                speak("Nasıl yardımcı olabilirim? ")
                voice = record().lower()
                response(voice)
                time.sleep(1)
                if voice in verilecekCevaplar.kapatcümle:
                    saat= datetime.datetime.now().strftime("%H")
                    if 7 < int(saat) < 18:
                            speak("İyi günler dilerim, hoşçakal.")
                            break
                    else:
                            speak("İyi geceler dilerim, hoşçakal.")
                            break
                if voice in "uyu":
                    saat= datetime.datetime.now().strftime("%H")
                    if 7 < int(saat) < 18:
                            speak("Bu saatte uyunur mu be! Ben gidiyorum.")
                            break
                    else:
                            speak("Teşekkürler")
                            time.sleep(2)
                            speak("Ahh, uyuyakalmışım. Ben uyumaya gidiyorum baaay!")
                            break
                else:
                    voice="ahmet"
        elif ses.issubset(set("senin adın ne kimsin sen".split())):
            speak("Benim adım Ahmet, senin asistanınım.")
        elif ses.issubset(set(verilecekCevaplar.yas.split())):
            speak(rd.choice(verilecekCevaplar.yasc))
        elif ses.issubset(set("sen nasılsın nasıl gidiyor hissediyorsun".split())):
            speak(rd.choice(nasil))
        elif "ben kimim".find(voice) == 0:
            global isim
            if isim == "q":
                speak("Henüz kim oldugunuzu bilmiyorum, bana isminizi bahşeder misiniz?")
                time.sleep(1)
                isim = record()
                speak(isim)
                return isim
            else:
                speak("İsminiz "+isim+" iyi çalışmalar.")
        elif voice == "instagram aç":
            speak("İnstagram açılıyor.")
            url = "https://instagram.com/"
            webbrowser.get().open(url)
            speak("İnstagram açıldı.")
        elif voice == "youtube'da ara":
            speak("Ne aramak istersin? ")
            voiceyutup = record().lower()
            search=voiceyutup
            url ="https://youtube.com/results?search_query="+voiceyutup
            webbrowser.get().open(url)
            speak(voiceyutup+" açıldı")
        elif "çal" in voice.split():
            datA = voice
            parcaismi = datA[:-4]
            speak(parcaismi+" açılıyor.")
            chromeOps = webdriver.ChromeOptions()
            chromeOps._binary_location = "C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"
            chromeOps._arguments = ["--enable-internal-flash"]
            global browser
            browser = webdriver.Chrome(r"C:\Users\berat\Desktop\Berat\pythoncod\chromedriver.exe",chrome_options=chromeOps)
            time.sleep(3)
            browser.get("https://www.youtube.com/results?search_query="+parcaismi)
            clickme = browser.find_element_by_xpath('//*[@id="video-title"]')
            clickme.click()
        elif voice == "google aç":
            sp.Popen(["C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"])
            speak("Google'ı açtım.")
        elif voice == "google kapat":
            os.system("taskkill /im chrome.exe /f")
            speak("Google'ı kapattım.")
        elif voice == "pencereyi kapat":
            pyautogui.hotkey("ctrl","w")
            speak("Pencere kapatıldı.")
        elif voice == "spyder aç":
            speak("Spyder açıldı.")
            sp.Popen([r"C:\Users\berat\anaconda3\pythonw.exe C:\Users\berat\anaconda3\cwp.py C:\Users\berat\anaconda3 C:\Users\berat\anaconda3\pythonw.exe C:\Users\berat\anaconda3\Scripts\\spyder-script.py"])
        elif voice == "zula aç":
            sp.Popen(["C:\LokumGames\Zula\zula_launcher.exe"])
            speak("Zula'yı açtım. Keyifli oyunlar dilerim.")
        elif voice == "minecraft aç":
            sp.Popen(["C:\Program Files (x86)\kisayollar\\Minecraft Team Extreme Launcher CRAZY TEAM.exe"])
            speak("Minecraft'ı açtım, keyifli oyunlar.")
        elif voice == "lol aç":
            sp.Popen(["C:\Riot Games\League of Legends\\LeagueClient.exe"])
            speak("Lol'u açtım, keyifli oyunlar. Tilt olma he")
        elif voice not in kelimeler:
            if voice not in hepsi:
                speak("Bunu googleda aratmamı ister misin?")
                voice3= record().lower()
                if "evet" in voice3:
                    search = voice
                    url = "https://google.com/search?q="+search
                    webbrowser.get().open(url)
                    speak(search+" ile alakalı googleda bulduklarım")
                    veriEkle(search,url)
                elif "hayır" in voice3:
                    speak("Tamamdır.")
                else:
                    speak("Anlamadım")

    def speak(string):
        tts = gTTS(string,lang="tr")
        rand = rd.randint(1,100000)
        file = "audio-"+str(rand)+".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)
    voice = record().lower()
    print(voice)
    if voice == "ahmet":
        response(voice=voice)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    