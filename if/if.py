# if 조건 : 
    # 실행 명령문

# weathre = "맑음";

# if weathre == "비" : 
#     print("우산이 필요해");
# elif weathre == "미세먼지" : 
#     print("마스크가 필요해");
# else : 
#     print("준비물이 필요없어.");

weathre = input("오늘 날씨는 어때 ? "); # input 함수는 사용자의 입력을 기다리는 함수. java 로 따지면 scanner 정도 ?
if weathre == "비" : 
    print("우산이 필요해");
elif weathre == "미세먼지" : 
    print("마스크가 필요해");
else : 
    print("준비물이 필요없어.");