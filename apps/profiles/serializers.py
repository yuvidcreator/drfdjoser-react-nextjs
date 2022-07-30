from rest_framework import serializers
from apps.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    pkid = serializers.CharField(source="get_user_id")
    id = serializers.UUIDField(source="get_user_uuid")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.CharField(source="user.full_name")
    email = serializers.CharField(source="user.email")
    mobile = serializers.CharField(source="get_mobile")
    bio = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(source="user.is_active")

    class Meta:
        model = Profile
        fields = [
            "pkid",
            "id",
            "email",
            "mobile",
            "first_name",
            "last_name",
            "full_name",
            "profile_picture",
            "date_of_birth",
            "gender",
            "bio",
            "address_line_1",
            "address_line_2",
            "city",
            "zip_code",
            "state",
            "country",
            "about_me",
            "is_mobile_verified",
            "is_verified_customer",
            "is_active",
            "is_admin",
            "is_manager",
            "is_customer"
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_admin:
            representation["is_admin"]=True

        if instance.is_manager:
            representation["is_manager"]=True
        
        return representation



class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "profile_picture",
            "date_of_birth",
            "gender",
            "bio",
            "address_line_1",
            "address_line_2",
            "city",
            "zip_code",
            "state",
            "country",
            "about_me",
        ]