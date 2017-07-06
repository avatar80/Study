# _*_ coding:utf-8 _*_

from sys import exit

def gold_room():
    print("황금으로 가득찬 방입니다. 얼마나 가져갈까요?")

    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("인간이여, 숫자쓰는 법부터 배우세요")

    if how_much < 50:
        print("좋아요 , 욕심부리지 않는군요. 당신이 이겼습니다.")
        exit(0)
    else:
        dead("용심쟁이 얼간이!@!")

def bear_room():
    print("여기는 곰한마리가 있습니다.")
    print("곰은 꿀을 잔뜩 들고 있습니다.")
    print("뚱뚱한 곰은 다른쪽 문앞에 있습니다.")
    print("어떻게 곰을 움직이겠습니까?")
    bear_moved = False

    while True:
        next = input(">")

        if next == "꿀 뺏기":
            dead("곰이 당신을 보더니 목이 떨어져라 따귀를 날립니다.")
        elif next == "곰 놀리기" and not bear_moved:
            print("곰이 문에서 비켜섰습니다. 이제 나갈 수 있습니다.")
            bear_moved = True
        elif next == "곰 놀리기" and bear_moved:
            dead("곰이 머리끝까지 열받아 당신의 다리를 씹어먹습니다.")
        elif next == "문 열기" and bear_moved:
            gold_room()
        else:
            print("무슨 말인지 모르겠어요")


def cthulhu_room():
    print("여기서는 대악마 크룰루를 봅니다.")
    print("기분이, 그것이, 아니 뭐든지 간에 당신을 쳐다보고 당신은 미쳐갑니다.")
    print("목숨을 위해 달아나려냐 네 머리를 먹어치우려냐?")

    next = input(">")

    if "달아나기" in next:
        start()
    elif "먹기" in next:
        dead("음, 맛이 좋군요")
    else:
        cthulhu_room()

def dead(why):
    print(why+" 잘했어요!")
    exit(0)

def start():
    print("어두운 방이 있습니다.")
    print("오른쪽과 왼쪽에는 문이 있습니다.")
    print("어느쪽을 고를까요?")

    next = input(">")

    if next == "왼쪽":
        bear_room()
    elif next == "오른쪽":
        cthulhu_room()
    else:
        dead("문 주위에서 맴돌기만 하다가 굶어 죽었습니다.")


start()




