from Artist.models import Artist_t, Work
from rest_framework import serializers

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    # user = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='username'
    #  )
    work = WorkSerializer(many=True)
    class Meta:
        model = Artist_t
        fields = ['name', 'user', 'work']
