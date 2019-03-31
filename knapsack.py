def knapsack(weight,profit,capacity):
    ratio=list(map(lambda w,p:p/w,weight,profit))
    index=[i for i in range(0,len(ratio))]
    index.sort(key=lambda i:ratio[i],reverse=True)
    orig_profit=0
    for j in index:
        if w<capacity and capacity>0:
            capacity-=weight[j]
            orig_profit+=profit[j]
        else:
            break
    if capacity>0:
        orig_profit+=profit[j]*(capacity/weight[j])
    return orig_profit
if __name__=='__main__':
    raw_weight=input("enter the  weight")
    raw_profit=input("enter the profit ")
    capacity=int(input("enter the capacity"))
    weight=[int(i) for i in raw_weight.split(" ")]
    profit=[int(i) for i in raw_profit.split(" ")]
    print(weight,profit)
    print(knapsack(weight,profit,capacity))

