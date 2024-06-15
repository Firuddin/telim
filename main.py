"""name = input("zehmet olmasa ad daxil edin")
print("salam"+name)"""

#name = """salam"""
#print(name)


"""student = input("ad daxil et")
teacher = input("dcsc")
actor = input("dcjndiu")
sentence = F'salam,o {student},salam o {teacher}.Salam,O {actor}'

print(sentence)"""

#game = "MainCraft"
#favorite_drink = "coffee"
#fruit = "grape"


#common = f"""
#this is favorite {game}
#this is favorite drink {favorite_drink}
#I love you {fruit}
#"""
#print(common)

"""
daxil edecem admin--> xos geldin cenab admin
daxil edecem user--> xos geldin cenab istifadeci
daxil edecem guest--> xos geldin cenab qonaq
daxil edecem ejbcuy--> zehmet olmasa duzgun ad daxil edin
"""


""" 
age -->alacaqsiz userden

age<18 olarsa imtahanda istirak ede bilmezsen
age = 18 olarsa imtahanda istirak ede bilersen
age>18 olarsa imtahanda istirak ede bilersen
"""

"""
name = input("zehmet olmasa ad daxil edin")

if name == "Admin":
    print("xos geldin cenab admin")
elif name == "User":
    print("xos geldin cenab istifadeci")
elif name == "Guest":
    print("xos geldin cenab qonaq")
else:
    print("zehmet olmasa duzgun ad daxil et")"""
    
    
"""
# --> //
# --> %
# --> **
# -->  
"""

"""new_list = ["Firudin aliyev","Hesen Huseynov","Salman hesimov","Cavid zerbiyev"]
istifadeci_sayi= 0
for name in new_list:
    istifadeci_sayi=istifadeci_sayi+1
    print(istifadeci_sayi,name)"""


#new_list = ["Firudin aliyev","Hesen Huseynov","Salman hesimov","Cavid zerbiyev"]

"""istifadeci_sayi = 0
for name in new_list:
    istifadeci_sayi=istifadeci_sayi+1
    ad = name.split()[0]
    soyad = name.split()[1]
    print('{}. istifadeci adi{} ve soyadi {}'.format(istifadeci_sayi,ad,soyad))"""
    
    
    
#new_list = ["Firudin aliyev","Hesen Huseynov","Salman hesimov","Cavid zerbiyev"]

"""istifadeci_sayi = 0

for name in new_list:
    istifadeci_sayi=istifadeci_sayi+1
    ad = name.split()[0]
    soyad =name.split()[1]
    print('{}. istifadeci adi {} ve soyadi {}'.format(istifadeci_sayi,ad,soyad))"""
    
    




new_list = ["Firudin aliyev","Hesen Huseynov","Salman hesimov","Cavid zerbiyev"]

moderator = "Hesen Huseynov"

istifadec_sayi=0
moderator_sayı=0

for name in new_list:
    ad =name.split()[0]
    soyad =name.split()[1]
    if name == moderator:
        moderator_sayı+=1
        print('{}.Moderator adi {} ve  soyadi {}'.format(moderator_sayı,ad,soyad))
    else:
        istifadec_sayi+=1
        print('{}.istifadeci adi {} ve soyadi {}'.format(istifadec_sayi,ad,soyad))