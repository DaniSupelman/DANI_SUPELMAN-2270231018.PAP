print("""

            SUUUPER CELL
    Menyediakan Pulsa dan Paket Data
    Jl.Swadaya Raya Jatiwaringin 
        Pondok Gede Kota.Bekasi
<==================================>
            ALL OPERATOR
T.SEL   INDOSAT     3    By.U   XL  SMARTFREN

PULSA : PPN Hanya 2000!!!
Rp.5.000     
Rp.10.000   
Rp.50.000 
Rp.100.000 

<==================================>
""")
nama=input("Nama Pembeli : ")
no = input("Masukkan no telp : ")
pesan=str(input("GOCENG? CEBAN? GOCAP? APA CEPE? : "))

if pesan == "GOCENG":
    harga=(5000)
elif pesan == "CEBAN":
    harga=(10000)
elif pesan == "GOCAP":
    harga=(50000)
elif pesan == "CEPE":
    harga=(100000)
else:
    pesan="-"
    harga= "-"
    pilihan=input("Pulsa Tidak Tersedia, silakan ulangi kembali Y/N ")
    

adm = 2000+harga

print("__________________________________________________")
print("Biaya /Pesanan : Rp.{}".format(harga))
print("ADM            : Rp.2000")
print("Total          :  Rp.{}".format(adm))
print("__________________________________________________")
print(""" Jika Ada Masalah Silahkan Hubungi
Telp.0858-5588-8855
Email : suuuper@cell.com
<======================TERIMA KASIH========================>""")