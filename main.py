# 예제 4-1 상하좌우

# 001 내 풀이
#n = int(input()) #공간만들기
#plan = list(map(str, input().split())) #움직임 기록
#count_plan = int(plan.count())
#point = (1,1) #시작위치
#print(point[0])

#for i in range(count_plan):

# 으아아악 안풀린다 일단 pass
# 그냥 해설 보기로함 ^^ 4-2풀어볼까 했는데 4-1못풀면 4-2도 못푸는거더라

# 4-1 답안예시

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시

# 예제 4-2 시각
n = int(input())
