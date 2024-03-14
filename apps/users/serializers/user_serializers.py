# Django
from django.contrib.auth import authenticate

# Rest Framework
from rest_framework import serializers

# Models
from apps.users.models import User


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ("password", "is_staff", "is_superuser", "groups", "user_permissions")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ("password", "is_staff", "is_superuser")

    @staticmethod
    def get_groups(instance):
        return instance.groups.all().values_list('name', flat=True)

    @staticmethod
    def get_user_permissions(instance):
        return instance.user_permissions.all().values_list('name', flat=True)

    def to_representation(self, instance):
        """Modifica la representación de la instancia"""
        representation = super().to_representation(instance)
        representation["groups"] = self.get_groups(instance)
        representation["user_permissions"] = self.get_user_permissions(instance)
        return representation


class UserWithPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "groups", "user_permissions", "last_login", "date_joined", "is_active")

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden."}
            )
        data.pop("confirm_password")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UpdatePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    def validate_current_password(self, value):
        user = authenticate(
            email=self.context['email'],
            password=value
        )
        if user is None:
            raise serializers.ValidationError("La contraseña actual es incorrecta.")
        return value

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"new_password": "Las contraseñas no coinciden."}
            )
        return data
