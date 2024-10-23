from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,blank=True,null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid conflict with auth.User
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permission_set",  # Avoid conflict with auth.User
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    
    def __str__(self):
        return self.username
    





    
class Student(models.Model):
    CLASS_CHOICES = [
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
        ('11', 'Class 11'),
        ('12', 'Class 12'),
    ]
    DIVISION_CHOICES = [
        ('A', 'Division A'),
        ('B', 'Division B'),
        ('C', 'Division C'),
        ('D', 'Division D'),
        ('E', 'Division E'),
    ]
    
    admission_no=models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    student_class = models.CharField(max_length=25,choices=CLASS_CHOICES)
    division=models.CharField(max_length=25,choices=DIVISION_CHOICES)
    
    
    def __str__(self):
        return f"{self.full_name} "
    
    
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('mystery', 'Mystery'),
        ('biography', 'Biography'),
        ('fantasy', 'Fantasy'),
        ('science', 'Science'),
        ('history', 'History'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    publication_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class LibraryHistory(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]

    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_histories')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='library_histories')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_name.full_name} - {self.book.title} ({self.status})"  
    
    def mark_as_returned(self):
        self.status = 'returned'
        self.returned_date = timezone.now()  # Make sure to import timezone
        self.save()



class FeeHistory(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.amount} - {self.payment_status}"
    
    def mark_as_paid(self):
        self.payment_status = 'paid'
        self.payment_date = timezone.now()  # Make sure to import timezone
        self.save()
        
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=12,default='')
    message=models.TextField()
    
    def __str__(self):
        return self.name