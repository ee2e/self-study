density = 20
brine = 100
water = 200

brine_density = ((density/brine)*100)/(brine+water) * 100

print(f'혼합된 소금물의 농도: {brine_density:.2f}%')