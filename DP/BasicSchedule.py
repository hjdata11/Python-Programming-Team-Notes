
# Weighted Job Scheduling Algorithm

def solution(table):
    sort_table = sorted(table, key=lambda x: x[1])

    profit = [p[2] for p in sort_table]
    acc_profit = [p[2] for p in sort_table]

    for i in range(1, len(profit)):
        for j in range(0, i):
            if sort_table[j][1] <= sort_table[i][0]:
                if acc_profit[j] + profit[i] > acc_profit[i]:
                    acc_profit[i] = acc_profit[j] + profit[i]

    maxProfit = 0
    for i in range(len(profit)):
        if maxProfit < acc_profit[i]:
            maxProfit = acc_profit[i]

    return maxProfit