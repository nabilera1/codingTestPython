import random

# 1부터 16까지의 숫자를 가진 리스트 만들기
numbers = list(range(1, 17))

# 각 팀의 구성원 수 설정
team_size = 2

# 총 팀 수 계산
num_teams = len(numbers) // team_size

# 각 팀 생성
teams = []
for team in range(num_teams):
    team_members = []
    for _ in range(team_size):
        chosen = random.choice(numbers)
        numbers.remove(chosen)
        team_members.append(chosen)
    teams.append(team_members)

# 팀 출력
for idx, team in enumerate(teams, start=1):
    # print(f'팀 {idx}: {team}번')
    print(f'팀 {idx}: {", ".join(map(str, team))}번')
