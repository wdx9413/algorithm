class Cut:
    def cut_rod(self, price_arr, sum):
        if sum == 0:
            return 0
        money = -1
        for item in price_arr:
            if sum >= item['cut_len']:
                money = max(money, item['cut_money'] + self.cut_rod(price_arr, int(sum - item['cut_len'])))
        return money
    def memorized_cut_rod(self, price_arr, sum):
        mem = [-1] * (sum + 1)
        def memorized_cut_rod_core(sum):
            if sum == 0:
                return 0
            if mem[sum] != -1:
                return mem[sum]
            money = -1;
            for item in price_arr:
                if sum >= item['cut_len']:
                    money = max(money, item['cut_money'] + memorized_cut_rod_core(sum - item['cut_len']))
            mem[sum] = money
            return money
        money = memorized_cut_rod_core(sum)
        return money
    def bottom_up_cut_rod(self, price_arr, sum):
        mem = [0] * (sum + 1)
        for i in range(1, sum + 1):
            money = -1
            for j in range(0, i):
                item = price_arr[j]
                money = max(money, item['cut_money'] + mem[i - item['cut_len']])
            mem[i] = money
        return mem[sum]
    def bottom_up_cut_rod2(self, price_arr, sum):
        #记录
        mem = [-1] * (sum + 1)
        mem[0] = 0
        s = [-1] * (sum+1)
        for i in range(1, sum + 1):
            money = -1
            for j in range(0, i):
                item = price_arr[j]
                if money < item['cut_money'] + mem[i - item['cut_len']]:
                    money = item['cut_money'] + mem[i - item['cut_len']]
                    s[i] = item['cut_len']
            mem[i] = money
        print(mem)
        print(s)
        return mem[sum]



if __name__ == "__main__":
    arr = [
            {'cut_len':1, 'cut_money':1},
            {'cut_len':2, 'cut_money':5},
            {'cut_len':3, 'cut_money':8},
            {'cut_len':4, 'cut_money':9},
            {'cut_len':5, 'cut_money':10},
            {'cut_len':6, 'cut_money':17},
            {'cut_len':7, 'cut_money':17},
            {'cut_len':8, 'cut_money':20},
            {'cut_len':9, 'cut_money':24},
            {'cut_len':10, 'cut_money':30}
        ]
    c = Cut()
    #print(c.cut_rod(arr, 4))
    #print(c.memorized_cut_rod(arr, 4))
    #print(c.bottom_up_cut_rod(arr, 4))
    print(c.bottom_up_cut_rod2(arr, 4))
