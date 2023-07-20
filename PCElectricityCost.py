pc_power_supply = int(input('How many watts is your power supply: '))
device_working_time = int(input('How many hours do you use your computer per day: '))

daily_cost_kwh = (pc_power_supply*device_working_time)/1000
month_cost_kwh = daily_cost_kwh*30

daily_cost_usd = daily_cost_kwh*0.170
month_cost_usd = month_cost_kwh*0.170

print('Daily cost of using your computer is around', daily_cost_usd,'USD')
print('Power in kWh(per day): ', daily_cost_kwh)
print('Power in kWh(per 30 days): ', month_cost_kwh)
month_question = input('Do u want to see what it cost monthly(yes or no)? ' )
if month_question == 'yes'.upper():
    print('Using your computer for 30 days for', device_working_time, 'hours a day will cost you about',month_cost_usd, 'USD')
else:
    print('GoodBye!')
elif currency == 'GBP':
    daily_cost_usd = daily_cost_kwh*0.34
    month_cost_usd = month_cost_kwh*0.34

    print('Daily cost of using your computer is around', daily_cost_usd,'GBP')
    print('Power in kWh(per day): ', daily_cost_kwh)
    print('Power in kWh(per 30 days): ', month_cost_kwh)
    month_question = input('Do u want to see what it cost monthly(yes or no)? ' )
    if month_question == 'yes'.lower():
        print('Using your computer for 30 days for', device_working_time, 'hours a day will cost you about',month_cost_usd, 'GBP')
    else:
        print('GoodBye!')
