number=[13,23,1322,43546,764,7,34,76,234,7578,4,2435,454,68,0,45,3546]
#sumthem them ussing loop
tota = 0
for i in number:
    tota+=i
print(tota)

#or
print(sum(number))

#finding the highest number in a list
print(max(number))
#or
max_score =0
for i in number:
    if i > max_score:
        max_score = i
print(max_score)

#lowets
print(min(number))