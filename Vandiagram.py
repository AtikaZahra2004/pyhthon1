#UNION----
s1={1,2,3,4,5}
s2={8,7,6,5,4}
s3=s1.union(s2)
s4=frozenset(s3)
print(s4)

d=eval(input('enter no.'))
print(d)
print(type(d))

# print(s1.union(s2))
print(s3)

#INTERSECTION----mid
print(s1.intersection(s2))

#DIFFERNCE-----phla s1
print(s1.difference(s2))

#SYMMETRIC------mid nhi ayega
print(s1.symmetric_difference(s2))

#INTERSECTION-UPDATE----midd
s1.intersection_update(s2)
print(s1)

#DIFFERNCE-UPDATE---set bta rh
s1.difference_update(s2)
print(s1)

#ISDISJOINT
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.isdisjoint(s2))

#SUBSET
print(s1.issubset(s2))


#ISSUPERSET
print(s1.issuperset(s2))


s1={1,2,3,4}
s2={1,2,3,4}
print(s1.issuperset(s2))
print(s1.issubset(s2))