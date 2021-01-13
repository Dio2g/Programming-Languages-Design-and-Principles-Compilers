passwordFile = {"user1":"password1",   
                "user2":"Pa$sW0rD123!",
                "user3":"madrid12$"}


username = input("enter username: ")
password = input("enter password: ")

if username in passwordFile :
  if passwordFile[username] == password :
    print("success")
  else :
    print("wrong password")
else :
  print("wrong user")

