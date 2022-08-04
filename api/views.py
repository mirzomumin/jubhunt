from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models

from .serializers import CategorySerializer, CompanySerializer, VacancySerializer, CandidateSerializer
from vacancy.models import Category, Company, Vacancy, Candidate

# Create your views here.



class StatisticsListView(APIView):
	def get(self, request):
		candidates_count = Candidate.objects.all().count()
		companies_count = Company.objects.all().count()
		vacancies_count = Vacancy.objects.all().count()
		content = {
			'Candidates count': candidates_count,
			'Companies count': companies_count,
			'Vacancies count': vacancies_count,
		}
		return Response(content)



class CategoryListView(generics.ListAPIView):
	serializer_class = CategorySerializer
	def get_queryset(self):
		queryset = Category.objects.annotate(
			candidates_count = models.Count('candidates'),
			salary = models.Case(
				models.When(
					(max(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_to')) /
					min(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_from')) >= 2),
					then=f"{(min(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_from'))) + (avg(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_from', 'salary_to')))/2} - {((max(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_to')))) + (avg(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_from', 'salary_to')))/2}"
					),
				models.When(
					(max(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_to')) /
					min(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_from')) < 2),
					then=f"{(avg(Candidate.objects.filter(category__id=models.OuterRef('id')).values('salary_from', 'salary_to')))}"
					),
			)
		)
		print(salary_dict)
		return queryset

# profile_title = Case(
# 				When(is_group=True, then=F('title')),
# 				When(is_group=False,
# 					then=CustomUser.objects
# 					.exclude(id=self.request.user.id)
# 					.filter(chat__id=models.OuterRef('id')))
# 					.values('username')[:1]),
# 				default=Value('None Title')),