# # # # print("hello world")
# # # # a ="hello"
# # # # num=10
# # # # @=10 not allowed
# # # # 2=2 not allowed
# # # # Age=22
# # # # age=23
# # # # print(Age)
# # # # print(age)
# # # # break=22 not allowed because break is a keyword in python
# # # # print=22 not allowed because print is a built-in function in python
# # # # print(print)

# # # # what is string 
# name ="Saksham"
# # # # print(name)
# print("my name is",name)
# # # # print(type(name))
# print("len of name is",len(name))

# # # # # indexing 
# # # # print(name[0])
# # # # print(name[2])
# print(name[len(name)-1])

# # # # slicing in python
# # # # name ="saksham"
# # # # print(name[0:3])

# # # # home work
# # # # reverse print String 
# # # # name = "Saksham"
# # # # new_name = name[::-1]
# # # # print(new_name)  

# # # ### operation 
# # # # name="saksham"
# # # # last="SHARMA"
# # # # upper_case=name.upper() #upper fn ka use upper case k liye krte h 
# # # # print(upper_case)
# # # # lower_case=last.lower() #lower fn ka use lower case k liye krte h
# # # # print(lower_case)


# # # # print(name.count("s")) #ye btata h vo char. kitni baar aaya h us string me

# # # # name="saksham"
# # # # last="SHARMA"
# # # # # print(name.title()) # first letter capital krne k liye use hota h
# # # # # print(name.capitalize()) # ye first letter capital krne k liye use hota h

# # # # print(name+last) # used to add strings
# # # # print(name+" "+last) # used to add space between strings

# # # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # # # list
# # # # lst = [1,2,2,3,4,5,6,7,"saksham",2.3]
# # # ### array vs list
# # # ###
# # # # mutable 
# # # # duplicated 
# # # # hetrogenous
# # # # order

# # # ### array
# # # # homogenous

# # # # print("my first list ",lst)
# # # # print("teh len of the list is ",len(lst))
# # # # print("type of list is ",type(lst))
# # # # print(lst[0])
# # # # print(lst[5])
# # # # print(lst[0:5])
# # # lst = [1,2,2,3,4,5,6,7,2.3]
# # # # lst.pop()  #last element ko remove
# # # # print(lst)
# # # # lst.append(100) #last me agr element add krna h to
# # # # print(lst)
# # # # lst.insert(0,1000)  #kisi specific jagah pe element daalna ho to
# # # # print(lst)
# # # # cpy=lst.copy() # to copy in other list
# # # # print(cpy)
# # # # lst.reverse()  # reverse the whole list
# # # # print(lst)
# # # # lst.remove(1000)  # to remove specific element 
# # # # print(lst)
# # # # lst.sort()   # agr list sort krna ho 
# # # # print(lst)
# # # # print(lst.count(2))   # agr kisi particular element ka count nikalna ho
# # # # print(lst)

# # '''
# # task
# # make a list
# # create a sub list inside that
# # now you have to access the element inside sublist
# # task_list = [1,2,3,4,[20,30,40],5,6,7,8]
# # print(task_list[4][1])  # this will print 30, as we are accessing the second element of the sublist at index 4
# # '''

# # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> tuple >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # # ordered 
# # # unchangeable
# # # heterogenous
# # # contains duplicate
# # # tpl = (1,2,3,4,5,585,5,"saksham",2.3)
# # # print("my first tuple - ",tpl)
# # # print("length of the tuple - ",len(tpl))
# # # print("type of the tuple tuple - ",type(tpl))

# # # indexing with tuple >>>>>>>>>
# # # print(tpl[0])
# # # print(tpl[2])
# # # print(tpl[0:6])
# # # print(tpl.count(5))
# # # task
# # # a=1,2,3,4,49,40,99   # by defualt tuple hi rhta h without paranthesis
# # # print(a)
# # # print(type(a))
# # # print(len(a))

# # # task
# # # tuple unpacking
# # # a,b,c=(1,2,3)
# # # print("below is tuple unpacking")
# # # print(a)
# # # print(b)
# # # print(c)
# # # this is also tuple unpacking
# # # a,b,c =1,2,3

# # # print("this is also is tuple unpacking")
# # # print(a)
# # # print(b)
# # # print(c)

# # # tepl=(1,2,3,4,5,6,7)
# # # print("max of the tuple is ",max(tepl))
# # # print("min of the tuple is ",min(tepl))
# # # print("sum of the tuple is ",sum(tepl))

# # # dictionary >>>>>>>>>>>>>>>>>>>>>
# # # unordered 
# # # unique
# # # mutable
# # my_dict={"name":"saksham","class":"3rd year","roll number":"23EJCIT139","address":"jaipur"}    
# # # name, class , roll number , address >>>>>>>> keys
# # # saksham , 3rd year , 23EJCIT139 , jaipur etc. are values 
# # # name: saksham is item
# # # print("my first dictionary ",my_dict)
# # # print("length of dictionary ",len(my_dict))
# # # print("type of the dictionary is ",type(my_dict))
# # # print(my_dict['name'])
# # # print(my_dict['class'])
# # # print(my_dict['roll number'])
# # # print(my_dict['address'])
# # # my_dict['address']="new jaipur"
# # # print(my_dict)
# my_dict={"name":"saksham","class":"3rd year","roll number":"23EJCIT139","address":"jaipur"}    
# my_dict['name']="rakesh"
# print(my_dict)     

# # '''my_dict={"name":"saksham","class":"3rd year","roll number":"23EJCIT139","address":"jaipur"}    
# # my_dict['branch']="IT"
# # print(my_dict)
# # my_dict.update({'age': '20'}) # this will update the dictionary with new key-value pairs
# # my_dict.update({'branch': 'CSE'}) # this will update the dictionary with new key-value pairs
# # print(my_dict)
# # # access using get function
# # print(my_dict.get("name")) # Saksham
# # print(my_dict.get("branch")) # IT
# # print(my_dict.get("age")) # Key not found, returns default value
# # print(my_dict.get("address")) # jaipur
# # print(my_dict.get("roll number")) # 23EJCIT139
# # # access using [] operator
# # print(my_dict["name"]) # Saksham
# # print(my_dict["branch"]) # IT
# # print(my_dict["age"]) # 20
# # print(my_dict["address"]) # jaipur
# # print(my_dict["roll number"]) # 23EJCIT139
# # '''
# # '''
# # task >>>>>>>>>>>>
# # update fn use kro and update dictionary  -- done
# # get function 5 example and [] k through kuch or bhi excess kro --

# # '''
# # # print("these are keys ",my_dict.keys());
# # # print("these are values",my_dict.values());
# # # print("these aere items ",my_dict.items());
# # # cpyDict=my_dict.copy()  # to copy the dictionary
# # # print("this is copied dictionary ",cpyDict)
# # # print(my_dict.clear());

# # # a=input("enter a number: ")
# # # print(a)
# # # print (type(a))
# # # b=input("enter a number: ")
# # # print(a*b)  # will give eror as a and b are strings

# # # type casting >>>>>>>>>>>>>>>

# # # a=int(input("enter a number: "))
# # # b=int(input("enter a number: "))
# # # print(a*b) 

# # # lst=[1,2,3,4,5,6,7,8,9]
# # # print("this is my list ",lst)
# # # print("type of list is ",type(lst))
# # # tpl =tuple(lst)  # converting list to tuple
# # # print("this is my tuple ",tpl)
# # # print("type of tuple is ",type(tpl))

# # # set >>>>>>>>>>>>>>>>>>>>>>
# # # unordered
# # # immutable
# # # unique
# # # myset={1,2,3,3,5,8,7,10,9,"saksham",2.3}
# # # print("this is my set ",myset)
# # # print("the length of set is ",len(myset))
# # # print("the type of set is ",type(myset))


# # ''' task>>>>>>>>>>>>>>>>>>>>>>>>>
# # myset.union()
# # myset.intersection()
# # myset.difference()'''
# # '''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# # print("union is ",set1.union(set2)) 
# # print("intersection is ",set1.intersection(set2))
# print("difference is ",set1.difference(set2))  
# # '''
# # # lst=list(myset) 
# # # lst.append(100) 
# # # print(set(lst))


# # '''tasks >>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # do operators on your own'''

