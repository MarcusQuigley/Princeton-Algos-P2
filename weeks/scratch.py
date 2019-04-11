#def oddTuples()

str = 'hello world'
  
print (str[::-1])
print (str[9:1:-1])
print (str[:-1])
print('----------')
print(str[::2])

t1 = (1,'two', 3)
t2 = (t1,'four')
print ((t1+t2)[3])
print ((t1+t2)[2:])
print ((t1+t2)[2:5])

print('----------')
print()
def applyToEach(list, func):
  #for i in list:
  #for i in list[:]:
  for i in list[0:len(list):1]:
    #print(i)
    print(func(i))


aList = ['w', 'pps',[10,2,33,33,32]]
applyToEach(aList, len)
# btuple = (44,'666','aad',[4,4,4])
# applyToEach(btuple, None)