# Calculate maximum profit

# price_list=[2,3,6,27,10,13,17]
price_list=[2,3,10,1,9,3,800]
profit=[]
i=0
step=1
subtract=0
print('*******************************')
# order O(n^2)
# while step<len(price_list):
#     temp=[]
#     while i<len(price_list)-1:
#         if i+step < len(price_list):
#             subtract=price_list[i+step]-price_list[i]
#             temp.append(subtract)
#             i+=1
#         else:
#             break
#     # print(f'temp={temp}')       
#     profit.append(max(temp))
#     step+=1
#     i=0
# print(f'profit={profit}')
# print(f'maximum profit={max(profit)}')

# order O(n)
price_list=[1,200,3,8,2,3000,1,50]
buy_price=price_list[0]
max_profit=0
candid=max(price_list)
for day in range(1,len(price_list)):
    if price_list[day]-buy_price > max_profit:
        max_profit=price_list[day]-buy_price
    if price_list[day]-candid > max_profit:
         max_profit=price_list[day]-candid
         buy_price=candid
    if price_list[day] < buy_price and price_list[day]< candid:
            candid=price_list[day]
    # print(f'***********candid={candid}')
print(f'maximum profit={max_profit}')


