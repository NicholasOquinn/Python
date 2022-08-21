Num_shares = 2000
Share_price1 = 40
Joe_paid = Num_shares * Share_price1
stock_comm = Joe_paid * 0.03
Share_price2 = 42.75
Joe_received = Num_shares * Share_price2
stock_comm2 = Joe_received * 0.03

print('Joe originally paid', Joe_paid)
print('Joe orignally paid his broker', stock_comm)
print('Joe sold the stock for', Joe_received)
print('Joe paid his broker for the second time', stock_comm2)