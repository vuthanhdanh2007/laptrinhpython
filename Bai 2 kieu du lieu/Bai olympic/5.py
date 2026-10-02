D,R,K,L = input().split()
D = int(D)
R = int(R)
K = int(K)
L = int(L)
chu_vi = 2*(D+R)
tong_coc = chu_vi // K
coc_moi_cay = L // K
print((tong_coc + coc_moi_cay - 1)// coc_moi_cay)
