from rest_framework import serializers
from conspect.models import ConspectModel, StructureComponentModel, AnswerModel, SubjectModel



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
        fields = ('name', 'owner', 'date_created', 'answers')


    # def create(self, validated_data):
    #     answers = validated_data.pop('answers')
    #     owner = validated_data.pop('owner')
    #     conspect = ConspectModel.objects.create(**validated_data)
    #     conspect.owner = str(owner)
    #     conspect.answers.set(answers)
    #     conspect.save()
    #     return conspect


    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.owner = validated_data.get('owner', request.user)
    #     instance.answers = validated_data.get('answers', instance.answers)
    #     instance.save()
    #     return instance



