from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def createUser(self, documentId, password=None):

        if not documentId:
            raise ValueError("Users must have an documentId ")
        user = self.model(documentId=documentId)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def createSuperUser(self, documentId, password):
        user = self.create_user(
            documentId=documentId,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    documentId = models.IntegerField('DocumentId',
                                     primary_key=True,
                                     null=False)
    name = models.CharField(max_length=45, null=False)
    lastName = models.CharField(max_length=45, null=False)
    cellularPhone = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=45, null=False)
    role = models.CharField('Role', max_length=20, null=False)
    password = models.CharField('Password', max_length=128, null=False)
    assignDoctor = models.ForeignKey('self',
                                     related_name='patient_document4',
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True)
    assignNurse = models.ForeignKey('self',
                                    related_name='patient_document5',
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True)
    assignRelative = models.ForeignKey('self',
                                       related_name='patient_document6',
                                       on_delete=models.SET_NULL,
                                       null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'documentId'