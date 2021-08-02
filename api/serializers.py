from rest_framework import serializers
from conspect.models import ConspectModel, StructureComponentModel, AnswerModel, SubjectModel



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConspectModel
        fields = ('name',)
        depth = 1


class StructureComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StructureComponentModel
        fields = ('name', 'subject',)
        depth = 1


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerModel
        fields = ('content', 'structure_component',)
        depth = 1


class ConspectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConspectModel
        fields = ('id', 'name', 'owner', 'date_created', 'answers')






