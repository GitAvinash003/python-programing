a=[123,"hello",5,"avinash"]
print(len(a))

b=[234,78,98,-78,23,-90]
print(len(b))
print(max(b))
print(min(b))
print(sorted(b))
print(sorted(b,reverse=True))

# indexing & slicing

a=['']
a[0]='start'
del(a[0])
print(a)

#slicing()

a=[123,"hello",5,"avinash"]
print(a[-1:-4])

#append(insert object in end of list)

a=[]
a.append(12)
print(a)
a.append(['a',12,'56'])
print(a)
a.append(45)
print(a)

#extend(iterable value inserting in list)
#insert(index based inserting in list)

a=[]
a.insert(0,'amit')
a.insert(1,'avinash')
a.insert(0,'vinash')
a.insert(3,45)
a.insert(2,90)
a.append('last')
a.extend([356])
a.insert(len(a),'last')

print(a)
print(len(a))

#count

x=['hello',43,'hello',67,'hello',98]
#print(x.count('hello'))
#clear
x.clear() #remove all in list

x=['hello',43,'hello',67,'hello',98]
print(x)
del(x[1:3])
print(x)
x.remove('hello')    #remove only first occurance
print(x)
for i in range(x.count('hello')):
    x.remove('hello')
print(x)
x.pop()    #remove last if value not give
print(x)

x=['hello',43,'hello',67,'hello',98]
x.pop(0)  #remove index 0 value
print(x)
