# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_manage_sys.settings')

# import django
# django.setup()

# import random
# from emsapp.models import *
# from faker import Faker
# import random
# import datetime

# fake = Faker()
# # depa = ['Human Resources','IT','Accounting','Finance','Marketing','Research','Development','Production']
# # roles = ['doctor','enginner','scientist','devloper','python devloper','java devloper','excutive','Team leader','Assistant Manager','Manager','Quility']
# def populate(N=50):
#     for entry in range(N):
#         fname = fake.first_name()
#         lname = fake.last_name()
#         salary = (random.randint(10000,40000))
#         Bonus = (random.randint(1000,9000))
#         phone = 9859874785
#         date = fake.date()
#         s = random.randint(18,25)
#         t = random.randint(1,9)


        


#         Employee.objects.get_or_create(first_name=fname,last_name=lname,salary=salary,Bonus=Bonus,dep_id=s,role_id=t,hire_date=datetime.date.today(),phone=phone)
# populate()

# #     first_name = models.CharField(max_length=100,null=False)
# #     last_name = models.CharField(max_length=100)
# #     dep = models.ForeignKey(Department,on_delete=models.CASCADE)
# #     salary = models.IntegerField(default=0)
# #     Bonus = models.IntegerField(default=0)
# #     role = models.ForeignKey(Role,models.CASCADE)
# #     phone = models.IntegerField(default=0)
# #     hire_date = models.DateTimeField(auto_now_add=False)

# # role = ['doctor','enginner','scientist','devloper','python devloper','java devloper','excutive','Team leader','Assistant Manager','Manager','Quility']

# # # for r in role:
# # #     rol = random.choice(role)
# # #     webpg = Role.objects.get_or_create(name = rol)

# # dep = ['Human Resources','IT','Accounting','Finance','Marketing','Research','Development','Production']

# # # for de in dep:
# # #     # dep = random.choice(dep)
# # #     city = fake.city()
# # #     Department.objects.get_or_create(name = random.choice(dep),location = city)
# # # dep = random.choice(dep)
# # # print(dep)

# # a = Department.objects.filter(id = 4)
# # print(a)
