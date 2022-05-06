def celcius_fahrenheit() :
    f = float(input("Masukkan derajat celcius :"))
    hasil = f * 9/5 + 32
    print ("suhu dalam fahrenheit =",(hasil),"derajat")
def celcius_reamur():
    r =float(input("Masukkan derajat celcius :"))
    hasil = r * 4/5
    print ("suhu dalam reamur =",(hasil),"derajat")
def celcius_kelvin():
    k =float(input("Masukkan derajat celcius :"))
    hasil = k + 273
    print ("suhu dalam kelvin =",(hasil),"derajat")
def kelvin_celcius():
    c =float(input("Masukkan derajat kelvin :"))
    hasil = c - 273
    print ("suhu dalam celcius =",(hasil),"derajat")
def kelvin_fahrenheit():
    f = float(input("Masukkan derajat dalam kelvin :"))
    hasil = 9/5 * (f-273) + 32
    print("suhu dalam fahrenheit =",(hasil),"derajat")
def kelvin_reamur():
    r = float(input("Masukkan derajat dalam kelvin :"))
    hasil = 4/5 * (r - 273)
    print ("suhu dalam reamur =",(hasil),"derajat")
def fahrenheit_celcius():
    c = float(input("Masukkan derajat dalam fahrenheit :"))
    hasil = 5/9 * c
    print ("suhu dalam celcius =",(hasil),"derajat")
def fahrenheit_kelvin():
    k = float(input("suhu dalam fahrenheit ="))
    hasil= (5/9 * (k - 32)) + 273
    print ("suhu dalam kelvin =",(hasil),"derajat")
def fahrenheit_reamur():
    r =float("Masukkan derajat dalam fahrenheit")
    hasil = 4/9 * (r-32)
    print ("suhu dalam reamur =",(hasil),"derajat")
def reamur_celcius():
    c = float(input("Masukkan derajat dalam reamur :"))
    hasil = 5/4 * c
    print ("suhu dalam celcius =", (hasil),"derajat")
def reamur_fahrenheit():
    f = float(input("Masukkan derajat dalam reamur :"))
    hasil = (9/4 * f) + 32
    print ("suhu dalam fahrenheit =",(hasil,"derajat"))
def reamur_kelvin():
    k = float(input("Masukkan derajat dalam kelvin :"))
    hasil = (5/4 * k) + 273

aksi = input("Mau konversi apa?(cf,cr,ck,kc,kf,kr,fc,fk,fr,rc,rf,rk) :")

if aksi == "cf":
    celcius_fahrenheit()
elif aksi == "cr":
    celcius_reamur()
elif aksi == "ck":
    celcius_kelvin()
elif aksi == "kc":
    kelvin_celcius()
elif aksi == "kf":
    kelvin_fahrenheit()
elif aksi == "kr":
    kelvin_reamur()
elif aksi == "fc":
    fahrenheit_celcius()
elif aksi == "fk":
    fahrenheit_kelvin()
elif aksi == "fr":
    fahrenheit_reamur()
elif aksi == "rc":
    reamur_celcius()
elif aksi == "rk":
    reamur_kelvin()
elif aksi == "rf":
    reamur_fahrenheit()
else :
    print ("ERROR===PERINTAH TIDAK DIKETAHUI===")