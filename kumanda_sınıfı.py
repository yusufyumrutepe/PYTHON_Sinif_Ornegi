import random
import time

class kumanda():
    def __init__(self,tv_durumu = "kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "trt"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_aç(self):
        if(self.tv_durumu == "açık"):
            print("tv zaten açık")
        else:
            print("tv açılıyor")
            self.tv_durumu = "açık"
    def tv_kapat(self):
        if(self.tv_durumu == "kapalı"):
            print("zaten kapalı")
        else:
            print("tv kapatılıyor")
            self.tv_durumu = "kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("sesi azaltmak için '<' basın artırmak için '>' basın")
            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("ses",self.tv_ses)
            if(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print("ses",self.tv_ses)
            else:
                print("ses güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)#aşağıda leni tanımladık
        self.kanal = self.kanal_listesi[rastgele]
        print("şu an ki kanal",self.kanal)
    def __len__(self): #burda len fonksiyonu class larda çalışmadığı için len i kendimiz tanımlıyoruz

        return len(self.kanal_listesi )
    def bilgilerigöster(self):
        print("tv durumu : {}  tv ses :  {} kanal listesi : {} şu anki kanal : {}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal))
kumanda1 = kumanda  #burada zaten init fonksiyonunda default olarak tanımlaöıştık o yüzden sıkıntı yok
print("""
1. tv aç
2. tv kapat
3. ses ayarları
4. kanal ekle
5. kanal sayısını öğrenme
6. rastgele kanal açma
7. televizyon bilgileri
çıkmak için "q"ya basın

""")
while True: # burada direk fonksiyonları çağırıyoruz seçilen işlem doğrultusunda fonksiyon üstte
    işlem = input("işlem seçiniz")
    if(işlem == "q"):
        print("program sonlandırılıyor")
        break
    elif(işlem == "1"):
        kumanda1.tv_aç()
    elif(işlem == "2"):
        kumanda1.tv_kapat()
    elif(işlem == "3"):
        kumanda1.ses_ayarları()
    elif(işlem == "4"):
        kanal_isimleri = input("kanal isimlerini giriniz")
        kanal_listesi = kanal_isimleri.split(",") #bu split özelliğini daha sonra göreceksin
        for eleman in kanal_listesi:
            kumanda1.kanal_ekle(eleman)
    elif(işlem == "5"):
        len(self.kanal_listesi)
        print("kanal sayısı",len(kumanda1))
    elif(işlem == "6"):
        kumanda1.rastgele_kanal()
    elif(işlem == "7"):
        kumanda1.bilgilerigöster()
    else:
        print("geçersiz işlem")

