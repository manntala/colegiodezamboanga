from django.db import models

# class Enrollment(models.Model):
#     student_no = models.CharField(max_length=100)
#     lrn_no = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     middle_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.TextField()
#     place_of_birth = models.CharField(max_length=100)
#     sex = models.CharField(max_length=10)
#     civil_status = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     age = models.IntegerField()
#     height = models.CharField(max_length=20)
#     weight = models.CharField(max_length=20)
#     religion = models.CharField(max_length=100)
#     contact_no = models.CharField(max_length=20)
#     level_of_education = models.CharField(max_length=50)


class Student(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    student_passcode = models.CharField(max_length=30, default='ccz_new_student')
    student_name = models.CharField(max_length=50, unique=True)
    student_gender = models.CharField(max_length=20, default='')
    student_contact = models.CharField(max_length=20, default='')
    student_age = models.IntegerField(default=0)
    student_address = models.CharField(max_length=50, default='')
    student_email = models.EmailField(max_length=50, default='')
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    year_id = models.ForeignKey('YearLevel', on_delete=models.CASCADE)
    session_id = models.ForeignKey('Session', on_delete=models.CASCADE)
    student_semester = models.CharField(max_length=20, default='')
    student_lrn = models.CharField(max_length=20, default='')
    student_placeofbirth = models.CharField(max_length=50, default='')
    student_dateofbirth = models.CharField(max_length=20, default='')
    student_civilstatus = models.CharField(max_length=15, default='')
    student_citizenship = models.CharField(max_length=20, default='')
    student_ethnicity = models.CharField(max_length=20, default='')
    student_height = models.FloatField(default=0.0)
    student_weight = models.FloatField(default=0.0)
    student_religion = models.CharField(max_length=20, default='')
    student_hsgrad = models.CharField(max_length=50, default='')
    student_hsyear = models.IntegerField(default=0)
    student_elemgrad = models.CharField(max_length=50, default='')
    student_elemyear = models.IntegerField(default=0)
    student_mothername = models.CharField(max_length=50, default='')
    student_motheredu = models.CharField(max_length=50, default='')
    student_motherattainment = models.CharField(max_length=50, default='')
    student_fathername = models.CharField(max_length=50, default='')
    student_fatheredu = models.CharField(max_length=50, default='')
    student_fatherattainment = models.CharField(max_length=50, default='')
    student_parentaddress = models.CharField(max_length=50, default='')
    student_statusofreg = models.CharField(max_length=20, default='')
    student_returnlastattended = models.CharField(max_length=20, default='')
    student_shiftfrom = models.CharField(max_length=50, default='')
    student_shiftto = models.CharField(max_length=50, default='')
    student_transferfrom = models.CharField(max_length=50, default='')
    student_entrancescore = models.CharField(max_length=10, default='')
    student_credentials = models.CharField(max_length=50, default='')
    student_scholarshipprivilege = models.CharField(max_length=50, default='')
    student_campus = models.CharField(max_length=30, default='')
    student_father_income = models.CharField(max_length=30, default='')
    student_mother_income = models.CharField(max_length=30, default='')
    student_emergency_contactname = models.CharField(max_length=50, default='')
    student_emergency_contactnumber = models.CharField(max_length=50, default='')
    student_emergency_contactaddress = models.CharField(max_length=50, default='')

    class Meta:
        indexes = [
            models.Index(fields=['student_campus']),
        ]

class Course(models.Model):
    pass
    # Define fields for Course model

class YearLevel(models.Model):
    pass
    # Define fields for YearLevel model

class Session(models.Model):
    pass
    # Define fields for Session model
