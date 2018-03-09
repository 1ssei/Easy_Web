from django.db import models

class Person(models.Model):
    birthday = models.DateTimeField('Birthday')
    name = models.CharField(max_length=50)

'''
*when you want to use ForeignKey, you can use here
*when you want to , you can use here
class Student(Person):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class = models.ForeignKey(Class, on_delete=models.CASCADE)
    ....
'''