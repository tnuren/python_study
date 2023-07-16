cabinet = {3: "유재석", 100: "김태호"};
print(cabinet[3]); # => "유재석" return
# print(cabinet[5]); # => 에러가 뜨고 서버 종료됨.
print(cabinet.get(5)); # => None 값을 return 하지만 서버가 종료되진 않음.
print(cabinet.get(3, "값이 없으면 ?"));


print(3 in cabinet);

cabinet[7] = "행운의 숫자";
print(cabinet);
del cabinet[7];
print(cabinet)

print(cabinet.keys());
print(cabinet.values());
print(cabinet.items());
