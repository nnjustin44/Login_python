import database_sqlite

database_sqlite.tables()
#database_sqlite.add_data()


user=raw_input('Username:')
password=raw_input('Password:')

database_sqlite.get_data()
database_sqlite.create_user(user,password)

if database_sqlite.get_data()==database_sqlite.tables():
    print("Welcome Back User")
else:
    new_user = raw_input('Create New Account Give Us A User Name: ')
    new_password = raw_input('Now Lets Get You A Password:')


"""ID=userID+" "+passwordID

if user+" "+password == ID:
    print ('Welcome Back ' + ID)
else :
    print( 'Welcome ' +new_user + new_password)
    userID.ID(new_user)
    passwordID.ID(new_password)"""