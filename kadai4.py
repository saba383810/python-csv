import csv

fd = open('KEN_ALL_1.csv')
csv_f = csv.reader(fd)
it = iter(csv_f)
bango = next(it)
ken = next(it)
chiho = next(it)
menseki = next(it)
jinko = next(it)
print("①　リスト menseki，および リスト jinko のデータを全て、文字から数値に変換しましょう。\n")
menseki = [int(menseki) for menseki in menseki]
jinko   = [int(jinko) for jinko in jinko]
print("変更完了！！")
#-----------------------------------------------------------------------------------------
print("\n②都道府県ごとに面積と人口を表示しましょう。\n")
for num in range(47):
    print(ken[num],"\n    面積:",menseki[num],"km^2\n    人口:",jinko[num],"千人")
#------------------------------------------------------------------------------------------
print("③面積の一番大きい都道府県、および一番小さい都道府県を表示しましょう。")

max_m = 0
min_m = 99999
min_n=0
for num in range(47):
    if max_m < menseki[num]:
        max_m = menseki[num]
        max_n = num
    if min_m > menseki[num]:
        min_m = menseki[num]
        min_n =num 
print("\n面積の一番大きい都道府県:",ken[max_n],"\n面積の一番小さい都道府県:",ken[min_n])
#-------------------------------------------------------------------------------------------
print("\n④人口の一番多い都道府県、および一番少ない都道府県を表示しましょう。")

max_j = 0
min_j = 1000000
min_n = 0
for num in range(47):
    if max_j < jinko[num]:
        max_j = jinko[num]
        max_n = num
    if min_j > jinko[num]:
        min_j = jinko[num]
        min_n =num
print("\n人口の一番多い都道府県   :",ken[max_n],"\n人口の一番少ない都道府県 :",ken[min_n])
#----------------------------------------------------------------------------------------------
print("\n⑤人口密度の一番高い都道府県、および一番低い都道府県を表示しましょう。")

max_den = 0
min_den = 1000000
min_n = 0

for num in range(47):
    den = jinko[num]/menseki[num]
    if den < max_den:
        max_den = den
        max_n = num
    if den > min_den:
        min_den = den
        min_n = num

print("\n人口密度の一番高い都道府県 :",ken[max_n],"\n人口密度の一番低い都道府県 :",ken[min_n])
#---------------------------------------------------------------------------------------------------
print("\n⑥地方ごとの、総面積、総人口、人口密度を表示\n")

jinko_den = 0
num =  0
while num < 46:
    menseki_sum = menseki[num]
    jinko_sum = jinko[num]
    while chiho[num]==chiho[num+1]:
        menseki_sum =  menseki_sum + menseki[num+1]
        jinko_sum = jinko_sum + jinko[num+1]
        num += 1
        if num==46:
            break
    jinko_den = round(jinko_sum/menseki_sum*1000 ,1)
    print(chiho[num]," \n    総面積   :",menseki_sum,"km^2 \n    総人口   :",jinko_sum,"千人  \n    人口密度 :",jinko_den,"人口/km^2") 
    num += 1
