from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	v = [
		('d','Select Your gender'),
		('M','Male'),
		('F','Female'),
	]
	p = [
		('G','Guest'),
		('D','Dietician'),
		('P','Person'),
	]
	gd = models.CharField(choices=v,default='d',max_length=5)
	mb = models.CharField(max_length=11)
	uq = models.CharField(max_length=10)
	role = models.CharField(choices=p,default='G',max_length=5)
	age=models.CharField(max_length=15)
	height=models.CharField(max_length=20)
	weight=models.CharField(max_length=25)
	is_dietician = models.BooleanField(default=False)
	is_person = models.BooleanField(default=False)

	pfimg = models.ImageField(upload_to='Profiles/',default='demoprofile.png')


class DProfile(models.Model):
	name = models.CharField(max_length=50)
	subjects = models.CharField(max_length=50)
	expr = models.IntegerField()
	designation = models.CharField(max_length=50)
	dch = models.OneToOneField(User,on_delete=models.CASCADE)

class PProfile(models.Model):
	age = [
		('0','Select Year'),
		('8-15','children'),
		('15-31','young age'),
		('32-55','middle age'),
		('55-above','post middle age'),
	]
	bmi = [
		('<25','underweight'),
		('>25','overweight'),
		('=25','Healthyweight'),
	]
	height=models.IntegerField
	weight=models.IntegerField
	# branch = models.CharField(max_length=50)
	age = models.CharField(default='0',choices=age,max_length=9)
	per = models.OneToOneField(User,on_delete=models.CASCADE)
	bmi = models.CharField(default='0',choices=bmi,max_length=9)
class Dietsuggestion(models.Model):
	age = [('0','Select Year'),
		('8-15','children'),
		('15-31','young age'),
		('32-55','middle age'),
		('55-above','post middle age'),
	]

	bmi = [
		('<25','underweight'),
		('>25','overweight'),
		('=25','Healthyweight'),
	]
	
	age = models.CharField(default='0',choices=age,max_length=9)
	bmi = models.CharField(default='0',choices=bmi,max_length=9)
	subject = models.CharField(max_length=50)
	descnote = models.CharField(max_length=10)
	ntfle = models.FileField(upload_to='DataFiles')
	date_created = models.DateField(auto_now=True)
	sckey = models.CharField(max_length=10)
	usr = models.ForeignKey(User,on_delete=models.CASCADE)

class ReqUsers(models.Model):
	p = [
		('0','Request'),
		('1','Done'),
		('2','Accepted'),
		('3','Rejected'),
		]
	# dt = models.ForeignKey(Dietsuggestion,on_delete=models.CASCADE)
	subject = models.CharField(max_length=50)
	desc = models.CharField(max_length=50)
	reqdate = models.DateField(auto_now=True)
	aprdate = models.DateField(auto_now=True)
	stsckey = models.CharField(choices=p,default='0',max_length=5)
	ststatus = models.CharField(choices=p,default='0',max_length=5)
	# models.CharField(choices=p,default='0',max_length=5)
#    per = models.ForeignKey(User,on_delete=models.CASCADE)
#    nts = models.ForeignKey(Notes,on_delete=models.CASCADE)


	# stsstatus =models.CharField(max_length=10)
	# pp = models.ForeignKey(User,on_delete=models.CASCADE)
	# tc = models.ForeignKey(User,on_delete=models.CASCADE)
	# write descnote or desc in ReqUser

class DietRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_made')
    dietician = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_received')
    request_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Diet Request from {self.user.username} to {self.dietician.username}'

