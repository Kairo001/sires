# Django
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    """Administrador de cuentas de usuario"""
    def _create_user(self, email, password, **extra_fields):
        """
        Crea y guarda un usuario con el correo electrónico y la contraseña.
        """
        if not email:
            raise ValueError("El correo electrónico es requerido.")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _("Correo electrónico"),
        max_length=128,
        unique=True,
        help_text=_("Correo electrónico del usuario. Requerido."),
        error_messages={
            "unique": _("Ya existe un usuario con este correo electrónico.")
        }
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Indica si el usuario puede acceder al sitio de administración."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designa si este usuario debe ser tratado como activo."
            "Desmarque esta casilla en lugar de eliminar la cuenta."
        ),
    )

    date_joined = models.DateTimeField(_("fecha de registro"), default=timezone.now)

    objects = UserAccountManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("usuario")
        verbose_name_plural = _("usuarios")

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Envía un correo electrónico a este usuario."""
        send_mail(subject, message, from_email, [self.email], **kwargs)