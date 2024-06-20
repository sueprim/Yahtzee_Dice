import random

# 야추 주사위 조합
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# 주사위 출력
def print_dice(dice):
    print("주사위:", dice)

# 점수 계산 함수
def score_upper_section(dice, number):
    return sum(die for die in dice if die == number)

def score_three_of_a_kind(dice):
    for number in range(1, 7):
        if dice.count(number) >= 3:
            return sum(dice)
    return 0

def score_four_of_a_kind(dice):
    for number in range(1, 7):
        if dice.count(number) >= 4:
            return sum(dice)
    return 0

def score_full_house(dice):
    counts = [dice.count(i) for i in range(1, 7)]
    if 3 in counts and 2 in counts:
        return 25
    return 0

def score_small_straight(dice):
    dice_set = set(dice)
    # Small straight: 4연속 주사위 눈이 있는지 확인
    for sequence in [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]:
        if all(number in dice_set for number in sequence):
            return 30
    return 0

def score_large_straight(dice):
    dice_set = set(dice)
    # Large straight: 5연속 주사위 눈이 있는지 확인
    for sequence in [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6)]:
        if all(number in dice_set for number in sequence):
            return 40
    return 0

def score_yahtzee(dice):
    if len(set(dice)) == 1:
        return 50
    return 0

def score_chance(dice):
    return sum(dice)

# 카테고리 이름 및 점수 함수 매핑
categories = {
    "ones": lambda dice: score_upper_section(dice, 1),
    "twos": lambda dice: score_upper_section(dice, 2),
    "threes": lambda dice: score_upper_section(dice, 3),
    "fours": lambda dice: score_upper_section(dice, 4),
    "fives": lambda dice: score_upper_section(dice, 5),
    "sixes": lambda dice: score_upper_section(dice, 6),
    "three_of_a_kind": score_three_of_a_kind,
    "four_of_a_kind": score_four_of_a_kind,
    "full_house": score_full_house,
    "small_straight": score_small_straight,
    "large_straight": score_large_straight,
    "yahtzee": score_yahtzee,
    "chance": score_chance,
}

# 각 플레이어의 점수 기록
def play_round(player, scores):
    print(f"{player}의 차례입니다!")
    dice = roll_dice()
    print_dice(dice)
    for i in range(2):
        reroll = input("다시 굴리시겠습니까? (y/n): ").strip().lower()
        if reroll == 'y':
            dice_to_reroll = input("다시 굴릴 주사위 인덱스(0-4, 콤마로 구분): ").strip()
            indices = [int(index) for index in dice_to_reroll.split(',')]
            for index in indices:
                dice[index] = random.randint(1, 6)
            print_dice(dice)
        else:
            break

    # 선택 가능한 카테고리 및 점수 계산
    available_categories = [cat for cat in categories if cat not in scores]
    print("선택 가능한 카테고리:", available_categories)

    chosen_category = input("선택할 카테고리: ").strip().lower()
    while chosen_category not in available_categories:
        print("유효한 카테고리를 선택하세요.")
        chosen_category = input("선택할 카테고리: ").strip().lower()

    score = categories[chosen_category](dice)
    scores[chosen_category] = score
    print(f"{chosen_category}에서 {score}점 획득!")

# 게임 종료 시 두 플레이어의 점수 합계를 계산
def calculate_final_score(scores):
    upper_score = sum(scores[cat] for cat in ["ones", "twos", "threes", "fours", "fives", "sixes"])
    if upper_score >= 63:
        upper_score += 35  # 보너스 점수
    lower_score = sum(scores[cat] for cat in categories if cat not in ["ones", "twos", "threes", "fours", "fives", "sixes"])
    return upper_score + lower_score

# 야추 게임
def play_yahtzee():
    scores_player1 = {}
    scores_player2 = {}
    round_number = 0

    while len(scores_player1) < len(categories):
        round_number += 1
        print(f"라운드 {round_number} - player1")
        play_round("player1", scores_player1)
        print(f"라운드 {round_number} - player2")
        play_round("player2", scores_player2)

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

# 야추 게임 실행
play_yahtzee()
