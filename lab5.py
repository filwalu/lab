# values=[10,20,30]
# keys=['ten','twenty','thirty']
# D = dict(zip(keys, values))
# # print(D)
#
# # values2=['thirty','forty','fifty']
# # keys2=[30,40,50]
# D2=dict(thirty=30, forty=40, fifty=50)
# D.update(D2)
# print(D)

values=[10,20,30]
keys=['ten','twenty','thirty']
d1 = {}
for i in range (3):
    d1[keys[i]] = values[i]
print(d1)