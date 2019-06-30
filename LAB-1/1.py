input = [( 'John', ('Physics', 80)) , ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
dict={}
l = []

#Displaying the dictionary before sorting
for key,value in input:
    dict.setdefault(key,[]).append(value)
print("Dictionary before sorting :",dict)

#Getting the values of the dictionary and storing then in separate list (dict_values)
dict_values = list(dict.values())

#Each value in dict_values is a list of tuples. Sorting the list based on the marks field in the tuple and storing them in another list (sorted_list)
for i in dict_values:
    sorted_list = sorted(i, key=lambda x: x[1],reverse=False)
    l.append(sorted_list)

#Replacing the old values in the list with new sorted values based on marks to their respective keys
i=0
for key in dict:
    dict[key] = l[i]
    i=i+1
print("Dictionary after sorting : ", dict)

