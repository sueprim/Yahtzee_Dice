# 야추 주사위 게임

**야추 주사위 게임** 에 오신 것을 환영합니다! 이 프로젝트는 클래식 주사위 게임인 야추를 구현한 것으로, 플레이어들이 주사위를 굴려 다양한 조합을 만들어 점수를 획득하는 게임입니다.

## 목차

- [개요](#개요)
- [게임 규칙](#게임-규칙)
  - [게임 준비](#게임-준비)
  - [게임 플레이](#게임-플레이)
  - [점수 계산](#점수-계산)
    - [상단 섹션](#상단-섹션)
    - [하단 섹션](#하단-섹션)
- [코드 설명](#코드-설명)
- [실행 방법](#실행-방법)

## 개요

야추는 5개의 주사위를 사용하여 다양한 조합을 만들고 점수를 획득하는 게임입니다. 운과 전략이 중요한 요소로 작용하며, 가족이나 친구들과 함께 즐기기 좋은 게임입니다. 닌텐도 스위치를 통해 알게 된 게임이고, 나름 재밌게 했던 기억이 있어 코드로 구현해보고 싶었습니다. 이로써 닌텐도 스위치가 없어도 컴퓨터로 야추 게임을 즐길 수 있습니다.

## 게임 규칙

### 게임 준비

- **주사위**: 5개
- **점수표**: 각 플레이어는 게임 시작 시 점수표를 받습니다.

### 게임 플레이

1. **첫 번째 굴림**: 플레이어는 5개의 주사위를 한 번 굴립니다.
2. **선택**: 플레이어는 원하는 주사위를 선택하여 재굴림할 수 있습니다.
3. **재굴림**: 선택한 주사위를 다시 굴립니다. 이 과정을 최대 두 번 더 반복할 수 있습니다.
4. **점수 기록**: 각 플레이어는 주사위를 굴린 후 점수표의 한 칸에 점수를 기록해야 합니다. 점수표에는 다양한 조합에 대한 점수 항목이 있습니다.

### 점수 계산

#### 상단 섹션

- 1의 합: 1이 나온 주사위 눈의 합
- 2의 합: 2가 나온 주사위 눈의 합
- 3의 합: 3이 나온 주사위 눈의 합
- 4의 합: 4가 나온 주사위 눈의 합
- 5의 합: 5가 나온 주사위 눈의 합
- 6의 합: 6이 나온 주사위 눈의 합

#### 하단 섹션

- **쓰리 오브 어 카인드 (Three of a Kind)**: 같은 숫자가 3개 이상 나온 경우, 주사위 눈의 총합
- **포 오브 어 카인드 (Four of a Kind)**: 같은 숫자가 4개 이상 나온 경우, 주사위 눈의 총합
- **풀 하우스 (Full House)**: 같은 숫자가 3개, 다른 숫자가 2개 나온 경우, 25점
- **스몰 스트레이트 (Small Straight)**: 연속된 숫자 4개 (예: 1-2-3-4), 30점
- **라지 스트레이트 (Large Straight)**: 연속된 숫자 5개 (예: 1-2-3-4-5), 40점
- **야추 (Yahtzee)**: 같은 숫자가 5개 나온 경우, 50점 (~***상남자들의 안식처***~)
- **찬스 (Chance)**: 주사위 눈의 총합 (~***겁쟁이들의 안식처***~)

### 보너스

- **상단 보너스**: 상단 섹션의 합이 63점 이상이면 35점의 보너스를 추가로 받습니다.


## 코드 설명

### 최초 실행시
```python
# 야추 게임 실행 함수
def play_yahtzee():
    scores_player1 = {}  # 플레이어 1의 점수를 저장하는 딕셔너리
    scores_player2 = {}  # 플레이어 2의 점수를 저장하는 딕셔너리
    round_number = 0

    # 각 플레이어가 모든 카테고리에 대해 점수를 기록할 때까지 게임을 진행
    while len(scores_player1) < len(categories):
        round_number += 1
        print(f"라운드 {round_number} - player1")
        play_round("player1", scores_player1)
        print(f"라운드 {round_number} - player2")
        play_round("player2", scores_player2)

# 야추 게임 실행
play_yahtzee()
```
각 플레이어들의 점수는 scores_player1, 2 에 저장이 되며 점수 categories를 다 채울때까지 while문을 돌려서 총 13 라운드를 진행하게 된다.

### 라운드 진행
```python
# 각 플레이어의 점수를 기록하는 함수
def play_round(player, scores):
    print(f"{player}의 차례입니다!")
    dice = roll_dice()  # 주사위를 굴림
    print_dice(dice)  # 주사위 결과를 출력
    for i in range(2):
        reroll = input("다시 굴리시겠습니까? (y/n): ").strip().lower()
        if reroll == 'y':
            dice_to_reroll = input("다시 굴릴 주사위 인덱스(0-4, 콤마로 구분): ").strip()
            indices = [int(index) for index in dice_to_reroll.split(',')]
            for index in indices:
                dice[index] = random.randint(1, 6)  # 선택한 주사위를 다시 굴림
            print_dice(dice)
        else:
            break

    # 선택 가능한 카테고리와 점수 계산
    available_categories = [cat for cat in categories if cat not in scores]
    print("선택 가능한 카테고리:", available_categories)

    chosen_category = input("선택할 카테고리: ").strip().lower()
    while chosen_category not in available_categories:
        print("유효한 카테고리를 선택하세요.")
        chosen_category = input("선택할 카테고리: ").strip().lower()

    score = categories[chosen_category](dice)  # 선택한 카테고리의 점수를 계산
    scores[chosen_category] = score  # 점수를 기록
    print(f"{chosen_category}에서 {score}점 획득!")

```
라운드가 시작되면 roll_dice() method를 통해 1 ~ 6사이의 랜덤 숫자 5개를 뽑고 print_dice()를 통해 뽑힌 주사위들을 볼 수 있다. 이 때 주사위를 다시 돌릴 기회를 총 2번 주고 reroll input 값이 'y' 가 들어오게 되면 다시 굴릴 주사위 index를 입력받아서 1~6사이의 랜덤숫자가 다시 배분되고 reroll input 값으로 'n' 가 들어오게 되면 break를 통해 for문을 나오게 된다. 그뒤 ```available_categories = [cat for cat in categories if cat not in scores]``` 를 통해 play_round() method의 인자로 입력받은 scores_player1, 2에 포함되지 않는 선택가능한 categories를 뽑아서 보여준다. 그후에 while문을 통해서 입력된 category의 유효성을 판단한다. 그후 람다 함수를 사용해 해당 카테고리로 현재 선택되어 있는 dice의 정보를 넘겨 점수를 계산한다. 그후 계산된 점수를 유저의 scores_player1, 2에 저장한다.

### 모든 라운드 종료
```python
# 야추 게임
def play_yahtzee():
    # 라운드 진행 코드 생략
    
    # 두 플레이어의 최종 점수 계산
    final_score_player1 = calculate_final_score(scores_player1)
    final_score_player2 = calculate_final_score(scores_player2)

    print(f"\n최종 점수:\nplayer1: {final_score_player1}점\nplayer2: {final_score_player2}점")

    # 승자 결정
    if final_score_player1 > final_score_player2:
        print("player1가 승리했습니다!")
    elif final_score_player2 > final_score_player1:
        print("player2가 승리했습니다!")
    else:
        print("무승부입니다!")

# 게임 종료 시 각 플레이어의 최종 점수를 계산하는 함수
def calculate_final_score(scores):
    upper_score = sum(scores[cat] for cat in ["ones", "twos", "threes", "fours", "fives", "sixes"])
    if upper_score >= 63:
        upper_score += 35  # 상단 보너스 점수
    lower_score = sum(scores[cat] for cat in categories if cat not in ["ones", "twos", "threes", "fours", "fives", "sixes"])
    return upper_score + lower_score
```
모든 라운드가 종료된 후에 각각의 player들의 점수를 계산하게된다. calculate_final)score() method를 통해 모든 카테고리에 대한 점수의 합을 구하고 여기서 upper_score 분이 63점 이상이면 35점의 보너스 점수를 획득하게 된다. 그 후 최종 점수를 보여주고 승자 or 무승부 표시를 해준다.

### 점수 계산 및 기타 코드
```python
# 주사위 굴림 함수: 5개의 주사위를 굴려 결과를 리스트로 반환
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# 주사위 출력 함수: 주사위 리스트를 출력
def print_dice(dice):
    print("주사위:", dice)

# 점수 계산 함수: 상단 섹션의 점수를 계산 (예: 1의 합, 2의 합 등)
def score_upper_section(dice, number):
    return sum(die for die in dice if die == number)

# 점수 계산 함수: Three of a Kind (같은 숫자 3개 이상) 점수 계산
def score_three_of_a_kind(dice):
    for number in range(1, 7):
        if dice.count(number) >= 3:
            return sum(dice)
    return 0

# 점수 계산 함수: Four of a Kind (같은 숫자 4개 이상) 점수 계산
def score_four_of_a_kind(dice):
    for number in range(1, 7):
        if dice.count(number) >= 4:
            return sum(dice)
    return 0

# 점수 계산 함수: Full House (같은 숫자 3개 + 같은 숫자 2개) 점수 계산
def score_full_house(dice):
    counts = [dice.count(i) for i in range(1, 7)]
    if 3 in counts and 2 in counts:
        return 25
    return 0

# 점수 계산 함수: Small Straight (4연속 숫자) 점수 계산
def score_small_straight(dice):
    dice_set = set(dice)
    for sequence in [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]:
        if all(number in dice_set for number in sequence):
            return 30
    return 0

# 점수 계산 함수: Large Straight (5연속 숫자) 점수 계산
def score_large_straight(dice):
    dice_set = set(dice)
    for sequence in [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6)]:
        if all(number in dice_set for number in sequence):
            return 40
    return 0

# 점수 계산 함수: Yahtzee (같은 숫자 5개) 점수 계산
def score_yahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    return 0

# 점수 계산 함수: Chance (모든 주사위 눈의 합) 점수 계산
def score_chance(dice):
    return sum(dice)

```

### 실행 방법
```
해당 repository를 clone
git clone https://github.com/sueprim/Yahtzee_Dice
.git
해당 프로젝트 파일로 이동
cd/../Yahtzee_Dice
python3 Yahtzee.py
이후 즐겁게 친구들과 플레이!!
```
