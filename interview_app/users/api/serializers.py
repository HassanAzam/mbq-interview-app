from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'created_at', 'updated_at',
            'name', 'password')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        print("!!!!!!!!")
        print(validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, data):
        '''
        Ensure the passwords are the same
        '''
        if data['password']:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data

    # class Meta:
    #     model = User
    #     fields = ["username", "email", "name", "url"]

    #     extra_kwargs = {
    #         "url": {"view_name": "api:user-detail", "lookup_field": "username"}
    #     }

