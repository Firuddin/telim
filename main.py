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
    
    




"""new_list = ["Firudin aliyev","Hesen Huseynov","Salman hesimov","Cavid zerbiyev"]

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
        print('{}.istifadeci adi {} ve soyadi {}'.format(istifadec_sayi,ad,soyad))"""
        
        
"""new_tuple =(1,2,3,4)
for number in new_tuple:
    print(number)"""
    
"""now_list =[[1,2],[3,4]]
for x,y in now_list:
    print(x,y)"""
    
"""last_list =["a","b","c","d","e"]
for index,harf in enumerate(last_list):
    if harf == "c":
     print("{} indexde {} herfi".format(index,harf))  """
     
     
     
     
"""telebeler = ["Ibrahim Huseynov","Musa Musayev","Seid Mert","Royal Vahabzade"]
for name in telebeler:
    print(name)"""



"""telebeler = ["Ibrahim Musayev","Kristiono Ronaldo","Lenoardo Mesi","Musayev Elvin"]

print(telebeler[2:])"""


"""numbers = [1,2,3,4,5,"6",7,8,9]

print(numbers[3:8])"""



"""telebeler = ["Ibrahim Musayev","Kristiono Ronaldo","Lenoardo Mesi","Musayev Elvin"]

for name in telebeler:
    print(name)"""
    
    
"""new_tuple = ("salam",1,2,4,"Eli")
for veli in new_tuple:
    print(veli)"""


"""telebeler = ["Ibrahim Huseynov", "Musa Musayev", "Seid Mert", "Royal Vahabzade"]


ad = telebeler[0].split()[0]
soyad = telebeler[0].split()[1]

print("bu şexsin adi {} ve soyadi {}".format(ad, soyad))"""




"""telebeler = ["Ibrahim Huseynov", "Musa Musayev", "Seid Mert", "Royal Vahabzade"]

Moderator ="Musa Musayev"
istiafdeci_sayi =0
for name in telebeler:
    istiafdeci_sayi+=1
    if Moderator ==name:
        print("istifadeci nomresi{} olan Moderator {}-dur".format(istiafdeci_sayi,name))
    else:
        print("istifadeci nomresi{} olan adi istifadeci {}-dur".format(istiafdeci_sayi,name))
"""

"""telebeler =("Ibrahim Huseynov", "Musa Musayev", "Seid Mert", "Royal Vahabzade")

for name in telebeler:
    print(name)"""
    
    
    
    
"""telebeler =("Ibrahim Huseynov", "Musa Musayev", "Seid Mert", "Royal Vahabzade")
moderator = "Musa Musayev"
istifadeci_sayi = 0
for name in telebeler:
    istifadeci_sayi+=1
    if name == moderator:
        print("moderator_sayi {} ve adi {}".format(istifadeci_sayi,name))
        pass
    else:
        print("istifadeci_sayi {} ve adi {}".format(istifadeci_sayi,name))"""



"""telebeler = ["Ali Huseynov","Huseyn Salmanli","Ilyas Ibadov","Resid Esrefov"]
istiafdeci_sayi = 0
for name in telebeler:
    istiafdeci_sayi+=1
    print(istiafdeci_sayi,name)"""
    
    
    
    
"""telebeler = ["Ibrahim Musayev","Kristiono Ronaldo","Lenoardo Mesi","Musayev Elvin"]
modertor ="Kristiono Ronaldo"
istifadeci_sayi = 0
for name in telebeler:
    istifadeci_sayi+=1
    if modertor == name:
        print("moderator nomresi {} ve adi{} ".format(istifadeci_sayi,name))
    else:
        print("istifadeci nomresi {} ve adi{} ".format(istifadeci_sayi,name))
"""


"""telebeler = ["Ibrahim Musayev","Kristiono Ronaldo","Lenoardo Mesi","Musayev Elvin"]
istifadeci_sayi = 0
for name in telebeler:
    istifadeci_sayi+=1
    ad = telebeler[0].split()[0]
    soyad = telebeler[0].split()[1]
    print("istifadeci nomresi {} telebenin adi {} ve soy adi {}".format(istifadeci_sayi,ad,soyad))"""



"""i = 0
while i<100:
   print(i)
   i+=1   #i=i+1
   
   
   
i=0
while i<100:
    i+=1
    if i ==50:
        continue
    print(i)
    """
    
    
    
"""for i in range(10):
    if i == 5:
        pass
    print(i)"""
    
    
x = "global x"

def fonk():
    y ="local y"
    print(y)
fonk()

print(x)