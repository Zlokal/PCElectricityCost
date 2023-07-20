pc_power_supply = int(input('How many watts is your power supply: '))
device_working_time = int(input('How many hours do you use your computer per day: '))
cost_kwh = float(input('How much is 1 KWh in your country: '))
currency = input('What currency did you use? ')

daily_cost_kwh = (pc_power_supply*device_working_time)/1000
month_cost_kwh = daily_cost_kwh*30

daily_cost = daily_cost_kwh*cost_kwh
month_cost = month_cost_kwh*cost_kwh

print('Daily cost of using your computer is around', daily_cost, currency)
print('Power in kWh(per day): ', daily_cost_kwh)
print('Power in kWh(per 30 days): ', month_cost_kwh)
month_question = input('Do u want to see what t cost monthly(yes or no)? ' )
if month_question == 'yes'.lower():
    print('Using your computer for 30 days for', device_working_time, 'hours a day will cost you about',month_cost, currency)
else:
    print('GoodBye!')
