import os

class Pengguna:
 def __init__(self, nm, no_induk):
  self.nama = str(nm);
  self.NoHp = str(no_induk);

 def getNama(self):
  return self.nama;

 def getNoHp(self):
  return self.NoHp;

 def setNama(self, nm):
  self.nama = nm;

 def setNoHp(self, no_induk):
  self.NoHp = no_induk;

DftrNama = {};
loop = True;

print("===================================");
print("=         Phone Book JTK          =");
print("===================================");
print("= #  MENU TAMPILAN                =");
print("= 1. Tambah Nama, No HP           =");
print("= 2. Hapus Nama, No HP            =");
print("= 3. Tampilkan Seluruh Pengguna   =");
print("= 4. Cari No HP                   =");
print("= 5. Edit Nama                    =");
print("= 6. Edit No HP                   =");
print("= 7. Jumlah No HP                 =");
print("= 0. Keluar                       =");
print("===================================");


while(loop):
  
 # membaca file txt
 if os.path.exists("phonebook.txt"):
  with open("phonebook.txt", "r") as file:
   for line in file:
    nama, no_hp = line.strip().split(",")
    pgn = Pengguna(nama, no_hp)
    DftrNama[no_hp] = pgn
    
 print("\n");
 menu = input("Masukan menu : ");

 if menu == "1":
  nama = str(input("Masukan nama : "));
  NoHp = str(input("Masukan no hp : "));
  pgn = Pengguna(nama, NoHp);
  DftrNama[NoHp] = pgn;
  # menyimpan ke file txt
  with open("phonebook.txt", "a") as file:
    file.write(f"{nama},{NoHp}\n")
    
 elif menu == "2":
  NoHp = str(input("Masukan no hp : "));
  if(NoHp in DftrNama):
   del DftrNama[NoHp];
   # menghapus dari file txt
   lines = []
   with open("phonebook.txt", "r") as file:
    lines = file.readlines()
   with open("phonebook.txt", "w") as file:
    for line in lines:
     nama, no_hp = line.strip().split(",")
     if no_hp != NoHp:
      file.write(line)
  else:
   print("Data tidak ditemukan!!!");
   
 elif menu == "3":
  for i in DftrNama:
   print("Nama  :", DftrNama[i].getNama());
   print("No hp :", DftrNama[i].getNoHp());
   
 elif menu == "4":
  NoHp = str(input("Masukan no hp : "));
  if(NoHp in DftrNama):
   print("Nama  : ", DftrNama[NoHp].getNama());
   print("No hp : ", DftrNama[NoHp].getNoHp());
  else:
   print("Data tidak ditemukan!!!");
   
 elif menu == "5":
  NoHp = str(input("Masukan no hp : "));
  if(NoHp in DftrNama):
   namaBaru = str(input("Masukan Nama Baru : "));
   DftrNama[NoHp].setNama(namaBaru);
   # Edit nama di file txt
   lines = []
   with open("phonebook.txt", "r") as file:
    lines = file.readlines()
   with open("phonebook.txt", "w") as file:
    for line in lines:
      nama, no_hp = line.strip().split(",")
      if no_hp == NoHp:
        line = f"{namaBaru},{no_hp}\n"
      file.write(line)
  else:
   print("Data tidak ditemukan!!!");
   
 elif menu == "6":
  NoHp = str(input("Masukan no hp : "));
  if(NoHp in DftrNama):
   NoHpBaru = str(input("Masukan No hp baru : "));
   DftrNama[NoHp].setNoHp(NoHpBaru);
   # Edit no hp di file txt
   lines = []
   with open("phonebook.txt", "r") as file:
    lines = file.readlines()
   with open("phonebook.txt", "w") as file:
    for line in lines:
      nama, no_hp = line.strip().split(",")
      if no_hp == NoHp:
        line = f"{nama},{NoHpBaru}\n"
      file.write(line)
   pgn = DftrNama[NoHp];
   DftrNama[NoHpBaru] = pgn;
   del DftrNama[NoHp];
  else:
   print("Data tidak ditemukan!!!");
   
 elif menu == "7":
  print("Jumlah pengguna : ", len(DftrNama));
  
 elif menu == "0":
  loop = False;
  
 else:
   print("Masukkan angka yang benar!!")