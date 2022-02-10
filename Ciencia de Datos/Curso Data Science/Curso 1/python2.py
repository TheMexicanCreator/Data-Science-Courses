#Ejercicio 1 (Lists)
a_list= [1, "hello", [1, 2, 3], True]
print(a_list[1])
print(a_list[1:4])

#Ejercicio 2
A= [1, 'a']
B= [2, 1, 'd']
print(A + B)

#Ejercicio 3 (Tuples)
tuple1= ("disco", 10, 1.2)
type(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
tuple2= tuple1 + ("hip hop", 10)
print(tuple2)
print(tuple2[0:3])
print(tuple2[3:5])
print(len(tuple2))

#Ejercicio 4
ratings= (0,2,1,5,4,3,8,7,6,9,10)
ratings_sorted= sorted(ratings)
print(ratings_sorted)

#Ejercicio 5
genres_tuple= ("pop","rock","soul","hip hop","metal","R&B","electronic","disco")
print(len(genres_tuple))
print(genres_tuple[3])
print(genres_tuple[3:6])
print(genres_tuple[0:2])
print(genres_tuple.index("disco"))

C_tuple= (-5,1,-3)
C_sorted= sorted(C_tuple)
print(C_sorted)

#Ejercicio 6 (Dictionaries)
soundtrack_dic= {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic.keys())
print(soundtrack_dic.values())

#Ejercicio 7
album_sales_dict= {"Back in Black":50, "The Bodyguard":50, "Thriller":65}
print(album_sales_dict.keys())
print(album_sales_dict["Thriller"])
print(album_sales_dict.values())

#Ejercicio 8 (Sets)
print(set['rap','house','electronic','rap'])

#Ejercicio 9
A= [1,2,2,1]
B= [1,2,2,1]
print(sum(A))
print(sum(B))

#Ejercicio 10
album_set1= set(["Thriller", "AC/DC", "Back in Black"])
album_set2= set(["Thriller", "Back in Black", "Dark Side of the Moon"])
album_set3= album_set1.union(album_set2)
print(album_set3)
print(album_set1.issubset(album_set3))

