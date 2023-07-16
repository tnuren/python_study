# 리스트

subway = [10, 20, 30];
print(subway);

# 30은 어디에 있나 ?
print(subway.index(30));

# 40 을 추가
subway.append(40);
print(subway);

# 50을 1 번째 index 에 추가.
subway.insert(1, 50);
print(subway);

# 객체를 뒤에서 하나 뺌
print(subway.pop())
print(subway)

# 10 몇개 인는지 찾아보자.
subway.append(10);
print(subway);
print(subway.count(10))

# 정렬 기능도 있다.
subway.sort();
print(subway);

# 지우기
subway.clear();
print(subway);

# 다양한 자료형을 함께 사용가능하다.
list = ["사용", 10, True];
print(list)

# 리스트를 합칠 수 있다.
subway.extend(list);
print(subway);