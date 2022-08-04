from django.db import models

# Create your models here.
class Base(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Category(Base):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Company(Base):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Vacancy(Base):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Candidate(Base):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='candidates')
	name = models.CharField(max_length=50)
	salary_from = models.PositiveIntegerField(default=0)
	salary_to = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name