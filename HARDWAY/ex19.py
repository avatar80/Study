# _*_ coding:utf-8 _*_

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("치즈가 %d개 있어요."%cheese_count)
    print("크래커가 %d상자 있어요."%boxes_of_crackers)
    print("파티 벌이기에 충분한 크기네요.")
    print("담요 한장 가져오세요.\n")

print("함수에 그냥 숫자 주기")
cheese_and_crackers(20, 30)

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
cheese_and_crackers(10+20, 5+6)
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

