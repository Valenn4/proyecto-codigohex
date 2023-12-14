from rest_framework import serializers
from calender.models import Activity
from authentication.models import User, Contact
from calender.models import Action, Music, Game

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserFeelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["feeling"]
        
class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    id_action = ActionSerializer()
    id_music = MusicSerializer()
    id_game = GameSerializer()
    
    class Meta:
        model = Activity
        fields = '__all__'
