lis = [1,1,0,-1,-1]
lis_pos = []
def plusMinus(arr):
    # Write your code here
    n = len(arr)
    for i in arr:
        if i > 0:
            lis_pos.append(i)
        if
































# s = input("your time: ")
# def convert_time(time):
#     # Разделение времени на часы, минуты и секунды
#     hh_mm_ss = time.split(':')
#     # Если время содержит AM
#     if 'AM' in hh_mm_ss[2]:
#         # Если часы равны 12, изменяем на 0
#         if hh_mm_ss[0] == '12':
#             hh_mm_ss[0] = '00'
#     # Если время содержит PM
#     else:
#         # Если часы не равны 12, добавляем 12
#         if hh_mm_ss[0] != '12':
#             hh_mm_ss[0] = str(int(hh_mm_ss[0]) + 12)
#     # Удаляем AM/PM из секунд
#     hh_mm_ss[2] = hh_mm_ss[2].replace('AM', '').replace('PM', '')
#     # Склеиваем часы, минуты и секунды в одну строку
#     return ':'.join(hh_mm_ss)
# print(convert_time(s))