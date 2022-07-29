from rest_framework import serializers
from apps.accounts.models import User
from djoser.serializers import UserCreateSerializer


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")
    email = serializers.SerializerMethodField()
    mobile = serializers.SerializerMethodField()
    gender = serializers.CharField(source="profile.gender")
    profile_photo = serializers.ImageField(source="profile.profile_picture")
    bio = serializers.TimeField(source="profile.about_me")
    date_of_birth = serializers.DateField(source="profile.date_of_birth")
    address_line_1 = serializers.CharField(source="profile.address_line_1")
    address_line_2 = serializers.CharField(source="profile.address_line_2")
    city = serializers.CharField(source="profile.city")
    pin_code = serializers.CharField(source="profile.zip_code")
    state = serializers.CharField(source="profile.state")
    country = serializers.CharField(source="profile.country")
    is_mobile_verified = serializers.BooleanField(source="profile.is_mobile_verified")
    is_customer_verified = serializers.BooleanField(source="profile.is_verified_customer")
    is_admin = serializers.BooleanField(source="profile.is_admin")
    is_manager = serializers.BooleanField(source="profile.is_manager")
    is_customer = serializers.BooleanField(source="profile.is_customer")

    class Meta:
        model = User
        fields = [ 
            "id",
            "pkid",
            "first_name", 
            "last_name", 
            "full_name", 
            "email", 
            "mobile", 
            "gender", 
            "profile_photo", 
            "bio", 
            "date_of_birth", 
            "address_line_1", 
            "address_line_2", 
            "city", 
            "pin_code", 
            "state", 
            "country", 
            "is_mobile_verified", 
            "is_customer_verified", 
            "is_admin", 
            "is_manager", 
            "is_customer",
        ]
    
    def get_first_name(self, obj):
        return obj.first_name.title()
    
    def get_last_name(self, obj):
        return obj.last_name.title()
    
    def to_representation(self, instance):
        represenatation = super(UserSerializer).to_representation(instance)
        if instance.is_superuser:
            represenatation["Admin"] = True
        return represenatation



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["pkid", "first_name", "last_name", "email", "mobile", "password"]