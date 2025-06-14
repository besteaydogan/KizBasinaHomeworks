#------------------------------------------------------------------
#girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul
sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Girilen sayı pozitif.")
elif sayi < 0:
    print("Girilen sayı negatif.")
else:
    print("Girilen sayı sıfır.")

#-------------------------------------------------------
#girilen sayının tek mi çift mi olduğunu yazan koşul
sayi = int(input("Bir sayı girin: "))

if sayi % 2 ==0:
    print("Girilen sayı çift.")
else:
    print("Girilen sayı tek.")

#------------------------------------------------------------------------
#Girilen nota göre harf aralığını yazan koşul (80-100 A, 60-80 B vs.)
while True:
    try:
        note = int(input("Lütfen 0 ile 100 arasında bir not girin: "))
        if 0 < note <= 100:
            print(f"Girilen not: {note}")
            break
        else:
            print("Hatalı giriş! Not 0 ile 100 arasında olmalıdır.")
    except ValueError:
        print("Geçersiz giriş! Lütfen bir sayı girin.")


if (79 < note <= 100):
    print("Your mark is A.")
elif (59 < note <= 80):
    print("Your mark is B.")
elif (39 < note <= 60):
    print("Your mark is C.")
else:
    print("Don't pass.")

#--------------------------------------------------------------------------------------------
#Girilen ismin karakter sayısı 5den büyükse "uzun bir isminiz var" değilse ismini yazsın
while True:
    names = input("İsminizi giriniz: ") # Kullanıcıdan ismi string olarak alır

    # İsmin uzunluğunu kontrol eder
    if len(names) > 5: # Eğer ismin karakter sayısı 5'ten büyükse
        print("Uzun bir isminiz var.")
        # Burada döngüden çıkmak isteyip istemediğinize karar verin.
        # Genellikle kullanıcıdan tekrar giriş beklenir veya döngü kırılır.
        # Eğer bu mesajı gösterip tekrar isim girmesini istiyorsanız 'break' koymayın.
        # Eğer sadece bu mesajı gösterip programdan çıkacaksa 'break' koyun.
        # Şu anki mantıkta, 'uzun bir isminiz var' dedikten sonra tekrar isim girmesini bekleyelim.
    elif len(names) > 0 and len(names) <= 5: # Eğer ismin karakter sayısı 1 ile 5 arasındaysa (dahil)
        print(f"İsminiz: {names}")
        break # Geçerli bir isim girildiği için döngüden çık
    else: # Kullanıcı boş bir isim girdiyse (len(names) == 0)
        print("Geçersiz giriş! Lütfen boş bırakmayın.")

#------------------------------------------------------------------------
#girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
sayi = int(input("Sayı giriniz: "))
adet = 0 # Bölen sayısını tutar
for i in range (1, sayi+1): # 1'den sayının kendisine kadar olan tüm sayıları kontrol eder
    if sayi%i==0: # Eğer sayı, i'ye kalansız bölünüyorsa
        adet+=1 # Bölen sayacını artır
if adet == 2: # Eğer sayının tam olarak 2 tane böleni varsa (1 ve kendisi)
    print(sayi, "asaldır.")
else:
    print(sayi, "asal değildir.")

#--------------------------------------------------------------------
# notlar=[45,85,75,50] içinde 75 değerinin indisini yazdıran döngü
notlar = [45, 85, 75, 50]
aranan_deger = 75
bulunan_index = -1 # Değer bulunamazsa -1 olarak kalır

for i in range(len(notlar)): # Listenin her bir indeksini dolaşır
    if notlar[i] == aranan_deger: # Eğer o indeksteki değer aranan değere eşitse
        bulunan_index = i # İndeksi kaydet
        break # Değeri bulduğumuz için döngüden çık

if bulunan_index != -1:
    print(f"{aranan_deger} değerinin indeksi: {bulunan_index}")
else:
    print(f"{aranan_deger} değeri listede bulunamadı.")

#-----------------------------------------------------
#girilen sayının faktöriyelini alalım. (for ve while)
sayi = int(input("Bir sayı girin: "))
faktoriyel = 1 # Faktöriyel değerini tutacak değişken. Çarpma işlemi olduğu için 1 ile başlarız.

# Negatif sayılar için kontrol
if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif sayi == 0:
    print("0! = 1")
else:
    # Sayı 1'den büyükse faktöriyel hesaplanır
    for i in range(1, sayi + 1): # 1'den sayının kendisine kadar döner (sayi dahil)
        faktoriyel *= i # faktoriyel = faktoriyel * i
    print(f"{sayi}! = {faktoriyel}")

#------------------------------------------------------------------------------------------------------------------------------------------------
#Kullanıcıdan pozitif bir sayı bekleyen, pozitifi de gördüğü an bastıran, negatif sayı girildikçe bir daha soran yapı kuralım. (for döngüsü ile)
sayi = int(input("Sayı giriniz: "))

# Sayı pozitif olmadığı sürece (yani sıfır veya negatif olduğu sürece) döngüye devam et
while sayi <= 0:
    print("Yanlış giriş! Sayı pozitif değil.")
    sayi = int(input("Lütfen poziti bir sayı giriniz: "))

print(f"Harika! Pozitif bir sayı girdiniz: {sayi}")

#-------------------------------------------------------------------------------------
#fonksiyon ile girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
import math

def asal_mi(sayi):
    # Asal sayılar 1'den büyük olmalıdır.
    if sayi <= 1:
        return False
    # 2, tek çift asal sayıdır.
    if sayi == 2:
        return True

    # Eğer sayı 2'den büyükse, 2'den başlayarak kareköküne kadar olan sayılara bak.
    # Eğer bu aralıkta herhangi bir sayıya bölünüyorsa, asal değildir.
    for i in range(2, int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:
            return False  # Bölündüğü an, asal olmadığını anlarız ve döngüden çıkarız.

    # Eğer döngü tamamlandıysa ve hiçbir sayıya bölünmediyse, asaldır.
    return True

# --- Kullanım Örnekleri ---
girilen_sayi = int(input("Bir sayı giriniz: "))

if asal_mi(girilen_sayi):
    print(f"{girilen_sayi} bir asal sayıdır.")
else:
    print(f"{girilen_sayi} bir asal sayı değildir.")

#-----------------------------------------------------------------
#fonksiyon ile girilen sayının faktöriyelini alalım. (for ve while)
def faktoriyel_hesapla(sayi):
    if sayi<0:
        return "Negatif sayıların faktöriyeli tanımlı değildir."
    elif sayi == 0:
        return 1
    else:
        carpim = 1  # Çarpma işlemi için başlangıç değerimiz 1
        for i in range(1, sayi + 1):  # 1'den sayının kendisine kadar olan tüm sayıları dolaş
            carpim *= i  # Her adimda çarpımı güncelledik
        return carpim  # Hesaplanan faktöriyel değerini döndürdük

# --- Kullanım Örnekleri ---
girilen_sayi = int(input("Faktöriyelini hesaplamak istediğiniz bir sayı girin: "))
sonuc = faktoriyel_hesapla(girilen_sayi)
print(f"{girilen_sayi}! = {sonuc}")