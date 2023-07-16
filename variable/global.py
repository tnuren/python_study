gun = 10;

def check(soldiers):
    global gun;
    gun = gun - soldiers;
    print("[함수 내] 남은 총 : {0}" .format(gun));

print("전체 총 : " + str(gun));
check(2);
print("남은 총 : " + str(gun));