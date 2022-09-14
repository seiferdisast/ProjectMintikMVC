from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    
        def createUser(self, documentId, password = None):
            if not documentId:
                raise ValueError("Users must have an documentId ")
            user = self.model(documentId = documentId)
            user.set_password(password)
            user.save(using=self._db)
            return user


        def createSuperUser(self, documentId, password):
            user = self.createUser(
                documentId = documentId,
                password = password,
            )
            user.is_admin = True
            user.save(using = self._db)
            return user

class User(AbstractBaseUser, PermissionsMixin):
    documentId = models.IntegerField('DocumentId', primary_key = True, max_length = 10, null = False)
    name = models.Charfield(max_length = 45, null = False)
    lastName = models.Charfield(max_length = 45, null = False)
    cellularPhone = models.Charfield(max_length = 10, null = False)
    address = models.Charfield(max_length = 45, null = False)
    email = models.Charfield(max_length = 45, null = False)
    role = models.Charfield('Role', max_length = 20, null = False)
    password = models.CharField('Password' , max_length = 8, null = False)
    assignDoctor = models.ForeignKey('self', on_delete = models.SET_NULL)
    assignNurse = models.ForeignKey('self', on_delete = models.SET_NULL)
    assignRelative = models.ForeignKey('self', on_delete = models.SET_NULL)

    def save(self,  **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'documentId'