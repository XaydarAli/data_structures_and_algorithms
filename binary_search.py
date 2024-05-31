def binary_search(list, item):
    low = 0
    high = len(list)-1
    count=0
    while low <= high:
        count += 1
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            print(guess)
            return mid
        if guess > item:
            print(guess)
            high = mid - 1
        else:
            print(guess)
            low = mid + 1
            print(f"{count} ta qadam ketdi")

    return None
myList = []
for i in range(1,100):
    myList.append(i)
(binary_search(myList,99))
""" Binary Search Algorithmini ishlatish uchun:
1)Binary Search ishlashi uchun ro'yxat tartiblangan bo'lishi shart!
2)Oldingi misolga qaytadigan bo'lsak , agar biz o'sha misolga binary algoritmini qo'llasak,
biz ikkiga bo'lish orqali ancha tezroq topamiz,linearda 99 ni topish uchun 99 qadam ketgan bo'lsa,
binaryda 7-qadamda topdi 99 sonini
"""