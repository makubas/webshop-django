from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user