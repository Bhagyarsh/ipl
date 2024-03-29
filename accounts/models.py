from datetime import timedelta
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from random import randint
from .utlis import random_string_generator, unique_key_generator
from django.db.models.signals import pre_save, post_save
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.utils import timezone

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # notice the absence of a "Password field", that's built in.
    objects = UserManager()
    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_verified(self):
        "Is the user a member of staff?"
        return self.Verified

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class EmailActivationQuerySet(models.query.QuerySet):
    def confirmable(self):
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
        end_range = now

        return self.filter(
            activated=False,
            forced_expired=False
        ).filter(
            timestamp__gt=start_range,
            timestamp__lte=end_range
        )


class EmailActivationManager(models.Manager):
    def get_queryset(self):

        return EmailActivationQuerySet(self.model, using=self._db)

    def confirmable(self):
        return self.get_queryset().confirmable()


class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=7)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = EmailActivationManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def can_activate(self):
        qs = EmailActivation.objects.filter(pk=self.pk).confirmable()
        if qs.exists():
            return True
        return False

    def activate(self):
        if self.can_activate():
            user = self.user
            user.Verified = True
            user.save()
            self.activated = True
            self.save()
            return True
        return False

    def regenerate(self):
        self.key = None
        self.save()
        if self.key is not None:
            return True
        return False

    def sent_activation_email(self):
        print(self.key)
        if not self.activated and not self.forced_expired:
            if self.key:
                base_url = getattr(settings, "BASE_URL", '')
                key_path = self.key
                path = "{base}{path}".format(base=base_url, path=key_path)
                context = {
                    "path": path,
                    "email": self.email
                }
                txt_ = get_template("emails/verify.txt").render(context)
                html_ = get_template("emails/verify.html").render(context)
                subject = '1-Click Email verifications'
                print(self.key)
                sent_mail_ = send_mail(
                    subject,
                    txt_,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[self.email],
                    html_message=html_,
                    fail_silently=False,
                )

                return sent_mail_
        return False

class Player(models.Model):
    User = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    points = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)

# pre_save.connect(pre_save_email_activation, sender=EmailActivation)

def user_post_save_user_create_reciever(sender, instance, created, *args, **kwargs):
    if created:
        
        if instance.first_name and instance.last_name :
            print(instance.get_full_name())
            obj = Player.objects.create(User=instance,name=instance.get_full_name())


def player_post_save_user_create_reciever(sender, instance, created, *args, **kwargs):
    if created:
        from qaformmatch.models import match,question
        from datetime import datetime
        ms = match.objects.filter(startdate = datetime.now().date())
        for field in ms:
            q = question.objects.create(
            match=field, team1=field.team_1,Player=instance, team2=field.team_2)
            
post_save.connect(player_post_save_user_create_reciever, sender=Player)
post_save.connect(user_post_save_user_create_reciever, sender=User)

