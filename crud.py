

### crud ---> c--> create , r ---> retrieve, u --> update , d---> delete
# from connecttion import  connectToDatbase
#
# connectionobj = connectToDatbase()
# if connectionobj:
#     print("--- connection successed ")
#     try:
#         query = "insert into students values (2, 'sdd');"
#         cursorobj = connectionobj.cursor()
#         cursorobj.execute(query)
#         connectionobj.commit()
#         connectionobj.close()
#     except Exception as e:
#         print(e)
#
# else:
#     print("------- error")
#########################
# from connecttion import  connectToDatbase
#
# connectionobj = connectToDatbase()
# if connectionobj:
#     print("--- connection successed ")
#
#     try:
#         id = int(input("please enter id: "))
#         name = input("please enter name: ")
#         query = f"insert into students values ({id}, '{name}');"
#         print(query)
#         cursorobj = connectionobj.cursor()
#         cursorobj.execute(query)
#         connectionobj.commit()
#         connectionobj.close()
#     except Exception as e:
#         print(e)
#
# else:
#     print("------- error")
######################### Prepared statement
# from connecttion import  connectToDatbase
#
# connectionobj = connectToDatbase()
# if connectionobj:
#     print("--- connection successed ")
#
#     try:
#         id = int(input("please enter id: "))
#         name = input("please enter name: ")
#         query = f"insert into students values (%s,%s);"
#         # print(query)
#         cursorobj = connectionobj.cursor()
#         cursorobj.execute(query, (id, name))
#         cursorobj.execute(query, (id+1,name))
#         connectionobj.commit()
#         connectionobj.close()
#     except Exception as e:
#         print(e)
#
# else:
#     print("------- error")
#################### update ####################################
# from connecttion import  connectToDatbase
#
# connectionobj = connectToDatbase()
# if connectionobj:
#     print("--- connection successed ")
#
#     try:
#         id = int(input("please enter id: "))
#         name = input("please enter name: ")
#         query = f"u"
#         # print(query)
#         cursorobj = connectionobj.cursor()
#         cursorobj.execute(query, (id, name))
#         cursorobj.execute(query, (id+1,name))
#         connectionobj.commit()
#         connectionobj.close()
#     except Exception as e:
#         print(e)
#
# else:
#     print("------- error")
#
#



























