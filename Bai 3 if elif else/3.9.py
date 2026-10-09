# Ví dụ khung giá:
# Km đầu tiên giá: 15000đ/km
# Từ km 2 đến 20 giá: 13500đ/km
# từ km 21 trở đi giá: 11000đ/km
km = float(input())
if km <= 1:
    tien = km * 15000
elif km <= 20:
    tien = 1 * 15000 + (km - 1) * 13500
else:
    tien = 1 * 15000 + 19 * 13500 + (km - 20) * 11000
print(tien)
