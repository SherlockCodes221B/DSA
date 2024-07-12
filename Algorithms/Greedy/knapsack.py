'''
Time complexity NlogN

Data Structre used here is List/Tuple

'''


class Knapsack():
    def __init__(self,weight, profit) -> None:
        self.weight = weight
        self.profit = profit
        self.cost = profit / weight
def knapsck(sack_weight,arr):
    arr.sort(key=lambda x:(x.profit/x.weight), reverse = True)
    final = 0
    for current_sack in arr:
        if current_sack.weight <= sack_weight:
            sack_weight -= current_sack.weight
            final += current_sack.profit
        else:
            final += current_sack.profit * sack_weight/current_sack.weight
    return final

if __name__ == "__main__":
    sack_weight = 50
    arr = [Knapsack(60,10), Knapsack(100,20), Knapsack(120,30) ]
    so_answer_is = knapsck(sack_weight,arr)
    print(f"Anwser is {so_answer_is}")
