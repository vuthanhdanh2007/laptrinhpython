kwh = float(input())
bac1 = min (kwh,50)
bac2 = max (kwh - 50, 0)
tien = bac1 * 1678 + bac2 * 2014
print(tien)
