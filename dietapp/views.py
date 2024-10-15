from django.shortcuts import render,redirect
from .forms import UsForm,Adrolech,DchPf,UsupForm,PForm,DietForm,ReqForm,DietRequestForm,CalculatorForm
from django.contrib import messages
from .models import User,DProfile,PProfile,Dietsuggestion,DietRequest
from django.core.mail import send_mail
from django.conf import settings
import secrets
import math

# Create your views here.

def home(request):
	return render(request,'diethtmls/home.html')

def about(request):
	return render(request,'diethtmls/about.html')

def contact(request):
	return render(request,'diethtmls/contact.html')

def register(request):
	if request.method == "POST":
		u = UsForm(request.POST)
		if u.is_valid():
			d=u.save(commit=False)
			messages.success(request,f"{d.username} User Created Successfully")
			d.save()
			return redirect('/login')
	else:
		u = UsForm()
	return render(request,'diethtmls/register.html',{'us':u})

def rolechange(request):
	k = User.objects.all()
	return render(request,'diethtmls/role.html',{'u':k})

def roleupdate(request,d):
	g = User.objects.get(id=d)
	if request.method == "POST":
		n = Adrolech(request.POST,instance=g)
		if n.is_valid():
			n.save()
			messages.success(request,"Role Updated Successfully")
			return redirect('/roles')
	n = Adrolech(instance=g)
	return render(request,'diethtmls/roleupdate.html',{'v':n})

def profile(request):
	return render(request,'diethtmls/profile.html')
def calculatebmi(request):
	return render(request,'diethtmls/calculatebmi.html')

def updateprofile(request):
	h = User.objects.get(id=request.user.id)
	d = []
	if h.role == 'D':
		c = DProfile.objects.filter(dch_id=request.user.id)
		for i in c:
			d.append(i.dch_id)
		if request.user.id not in d:
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				s = DchPf(request.POST,instance=h)
				if v.is_valid() and s.is_valid():
					n = v.save(commit=False)
					n.is_dietician = 1
					n.save()
					r = s.save(commit=False)
					r.dch_id = request.user.id
					r.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			s = DchPf()
			return render(request,'diethtmls/upprofile.html',{'y':v,'n':s})
		else:
			f = DProfile.objects.get(dch_id=request.user.id)
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				s = DchPf(request.POST,instance=h)
				if v.is_valid() and s.is_valid():
					v.save()
					s.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			s = DchPf(instance=h)
			return render(request,'diethtmls/upprofile.html',{'y':v,'n':s})
	elif h.role == 'P':
		x = PProfile.objects.filter(per_id=request.user.id)
		u = []
		for i in x:
			u.append(i.per_id)
		if request.user.id not in u:
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				g = PForm(request.POST)
				if v.is_valid() and g.is_valid():
					a = v.save(commit=False)
					a.is_person = 1
					a.save()
					e = g.save(commit=False)
					e.per_id=request.user.id
					e.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			g = PForm()
			return render(request,'diethtmls/upprofile.html',{'y':v,'d':g})
		else:
			q = PProfile.objects.get(per_id=request.user.id)
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				g = PForm(request.POST,instance=q)
				if v.is_valid() and g.is_valid():
					v.save()
					g.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			g = PForm(instance=q)
			return render(request,'diethtmls/upprofile.html',{'y':v,'d':g}) 
	else:
		pass
def dietlist(request):
	n = Dietsuggestion.objects.filter(usr_id=request.user.id)
	if request.method == "POST":
		c =DietForm (request.POST,request.FILES)
		if c.is_valid():
			z = c.save(commit=False)
			z.sckey = secrets.token_hex(2)
			z.usr_id = request.user.id
			z.save()
			messages.success(request,"Diet Added Successfully")
			return redirect('/diet')
	c = DietForm()
	return render(request,'diethtmls/dietsuggestion.html',{'p':c,'z':n})	
def dietdisp(request):
	y = Dietsuggestion.objects.filter(age=request.user.pprofile.age,bmi=request.user.pprofile.bmi)
	h,m,d,w = {},{},{},0
	for j in y:
		h[j.id] = j.subject,j.usr_id,j.descnote,j.date_created,j.id
	b = User.objects.all()
	for p in b:
		m[p.id] = p.email,p.username,p.pfimg,p.id
		# print(m.values())
	for i in h.values():
		# if i[1] in m:
		# 	d[i[4]] = i[0],i[2],i[3],m[1][0],m[1][1],m[1][2]
		if(i[1] in m.keys()):
			d[w] = i[0],i[2],i[3],m[i[1]][0],m[i[1]][1],m[i[1]][2],i[4]
			w+=1
	# print(d)
		# z = User.objects.filter(id=i[-1])
		
		# print(i[-1],z)
		# if i[-1] == z:
		# 	print(z.username,z,i[0],i[1],i[2])


		# print(i,type(i))
	# for j in y:
		# print(j.age,j.bmi,j.subject)
	return render(request,'diethtmls/dietdisplay.html',{'a':d.values()})

def dietreq(request,u):
	t = Dietsuggestion.objects.get(id=u)
	k = ReqForm(instance=t)
	return render(request,'diethtmls/dietrequest.html',{'n':k})
def diet_request_view(request):
    if request.method == 'POST':
        form = DietRequestForm(request.POST)
        if form.is_valid():
            diet_request = form.save(commit=False)
            diet_request.user = request.user
            diet_request.save()

            # Notify the dietician
            notify_dietician(diet_request)

            messages.success(request, 'Your diet request has been sent.')
            return redirect('success_page')
    else:
        form = DietRequestForm()

    return render(request, 'diethtmls/diet_request.html', {'form': form})

def notify_dietician(diet_request):
    subject = 'New Diet Request'
    message = f'You have received a new diet request from {diet_request.user.username}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [diet_request.dietician.email]  # Send to the selected dietician
    send_mail(subject, message, email_from, recipient_list)
def success_page(request):
    return render(request, 'diethtmls/success.html')
def calculator(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operation = form.cleaned_data['operation']

            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                if number2 != 0:
                    result = number1 / number2
                else:
                    result = 'Error: Division by zero'
            elif operation == 'power':
                result = number1 ** number2
            elif operation == 'sqrt':
                result = math.sqrt(number1)  # Square root of number1
            elif operation == 'percent':
                result = (number1 * number2) / 100  # Percentage of number1
    else:
        form = CalculatorForm()

    return render(request, 'calculatebmi.html', {'form': form, 'result': result})


 