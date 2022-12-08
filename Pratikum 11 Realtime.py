# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:36:58 2022

@author: Rafif Fernanda
"""

print("~~Biodata Mahasiswa~~")

class biodata():
    empCount = 0
    def init(self,nama,nim,angkatan):        
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
    
    def disp_input(self):
        self.nama = input("Masukan Nama anda: ")
        self.nim = input("Masukan NIM anda: ")
        self.angkatan = input ("Angkatan: ")
        biodata.empCount +=1
        
    def disp_count(self):
        print("Jumlah Mahasiswa %d" % biodata.empCount)
 
    def disp_biodata(self):
        print ("Biodata anda: ")
        print ("Nama: ", self.nama)
        print ("NIM: ", self.nim)
        print ("Angkatan: ", self.angkatan)
        
datamhs = biodata()
datamhs.disp_input()
datamhs.disp_biodata()
print("Total Mahasiswa: %d" % biodata.empCount)
