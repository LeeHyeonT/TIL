from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title',)

class ArtistSerializer(serializers.ModelSerializer):
    # 사용할 serializer 안에 넣어서 custom 하여 사용하자!
    class MusicListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = ('title',)

    music_set = MusicListSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    
    class Meta:
        model = Artist
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist',)
        read_only_fields = ('artist',)
