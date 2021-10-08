

#https://riptutorial.com/algorithm/example/23962/weighted-job-scheduling-algorithm


def solution(table):
    sort_table = sorted(table, key=lambda x : x[1])

    profit = [p[2] for p in sort_table]
    acc_profit = [p[2] for p in sort_table]

    for i in range(1, len(profit)):
        for j in range(0, i):
            if sort_table[j][1] <= sort_table[i][0]:
                if acc_profit[j] + profit[i] > acc_profit[i]:
                    acc_profit[i] = acc_profit[j] + profit[i]

    return max(acc_profit)

print(solution([[3, 6, 3], [2, 4, 2], [10, 12, 8], [11, 15, 5], [1, 8, 10], [12, 13, 1]]))