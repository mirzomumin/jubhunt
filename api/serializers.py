from rest_framework import serializers

from vacancy.models import Category, Company, Vacancy, Candidate



class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
	class Meta:
		model = Vacancy
		fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Candidate
		fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
	candidates_count = serializers.IntegerField()
	salary = serializers.StringRelatedField()
	class Meta:
		model = Category
		fields = '__all__'
