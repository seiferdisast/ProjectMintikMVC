from django.db import models
from dhango.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
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
    documentId = models.Charfield('DocumentId', primary_key = True)
    name = models.Charfield(45)
    lastName = models.Charfield(45)
    cellularPhone = models.Charfield(10)
    address = models.Charfield(45)
    email = models.Charfield(45)
    role = models.Charfield(20)
    password = models.CharField('Password' , max_length = 8)
    assignDoctor = models.ForeignKey('self', on_delete = models.SET_NULL)
    assignNurse = models.ForeignKey('self', on_delete = models.SET_NULL)
    assignRelative = models.ForeignKey('self', on_delete = models.SET_NULL)

    def save(self,  **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'documentId'