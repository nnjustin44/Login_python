import Username_list.py as list
#import userpass_list as up

user=raw_input('Username:')
password=raw_input('Password:')

new_user=raw_input('Create New Account Give Us A User Name: ')
new_password=raw_input('Now Lets Get You A Password:')

ID=userID+" "+passwordID

if user+" "+password == ID:
    print ('Welcome Back ' + ID)
else :
    print( 'Welcome ' +new_user + new_password)
    userID.ID(new_user)
    passwordID.ID(new_password)