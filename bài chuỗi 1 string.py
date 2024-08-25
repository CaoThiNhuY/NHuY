# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:15:35 2024

@author: Admin
"""

#1
print(' Đại học Quốc gia \n Khu phố 6 \n P. Linh Trung \n Q. Thủ Đức \n Tp. HCM')
#2
chuoi=("Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM")
print(chuoi.replace(',','\n').replace('P.','').replace('Q.','').replace('Tp.',''))