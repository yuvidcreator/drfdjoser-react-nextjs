from rest_framework import serializers
from apps.profiles.models import (Employee, Manager, Accountant, Salesman, Customer, OTP, PasswordResetToken)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"


class AccountantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountant
        fields = "__all__"


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OTPSerializers(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = "__all__"


class PasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetToken
        fields = "__all__"