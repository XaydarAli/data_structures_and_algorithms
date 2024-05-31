def findNum(N=100):
    for n in range(1,100):
        answer = input(f"Siz {n} sonini o'yladingizmi ? (yes/no) \n")
        if answer.lower()=='yes':
            print("I found the number !")
            return n
findNum()
"""Linear searchni ishlatish qachon afzal:
1)Ro'xyat tartiblanmagan bo'lsa
2)Ro'yxatdagi elementlar soni kam bo'lsa
3) Linear search algoritmi orqali ro'yxatdan,
biror elementni qidirmoqchi bo'lsak,ro'yxatni boshidan oxirigacha qidirib chiqadi.
Yuqorida yozilgan koddan ko'rishimiz mumkinki ,o'ylangan sonni topish uchun bitta bitta so'rab chiqadi.
Linear searchning kamchiligi shundaki agar 99 soni o'ylangan bo'lsa , 99 sonini topish uchun 99 ta qadam ketadi
"""