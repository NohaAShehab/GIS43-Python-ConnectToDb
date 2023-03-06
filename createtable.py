from connecttion import connectToDatbase

connectionobj = connectToDatbase()
if connectionobj:
    print("--- connection successed ")
    try:
        query = "create table students(id serial primary key, name varchar(40)); "

        ## create from connection database cursor
        dbcrusor = connectionobj.cursor()
        dbcrusor.execute(query)
        connectionobj.commit()

        print("----- table created ")
        connectionobj.close()
    except Exception as e:
        print(e)

else:
    print("------- error")