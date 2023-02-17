def create(self,validated_data):
  return User.objects.create_user(**validated_data)


def update(self,instance,validated_data):
  instance.username = validated_data('username',instance.username)
  instance.save()
  return instance
#========================================
# example of updating a user instance.
def update(self,instance,validated_data):
  # we delete the password from vaidated_data dictionary and set it None because user might not change the password.
  #- and asign it to password variable to access that later. 
  #- becuast the password have to be saved using set_password() method.
  password = validated_data.pop('password',None)  
  user = super().update(instance,validated_data)
  
  if password:
    user.set_password(password)
    user.save()
    
  return user
