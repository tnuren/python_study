# while
# 조건이 만족할 때 까지 반복

# customer = "토르";
# index = 5;

# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요" .format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.");


# 무한 루프
customer = "아이언맨";
index = 1;
while True:
    print("{0}, 커피가 준비 되었습니다. {1} 번 호출했습니다." .format(customer, index))
    index += 1
