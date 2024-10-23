# core/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Student,Book,LibraryHistory,FeeHistory,Contact

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'email']  # Exclude password fields

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(UpdateBookForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
class AddLibraryHistoryForm(forms.ModelForm):
    class Meta:
        model=LibraryHistory
        fields='__all__'
        widgets = {
              'returned_date': forms.DateInput(attrs={'type': 'date'}),
              
          }
        
    def __init__(self, *args, **kwargs):
        super(AddLibraryHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
            
class FeeHistoryForm(forms.ModelForm):
    class Meta:
        model=FeeHistory
        fields='__all__'
        
        widgets = {
              'due_date': forms.DateInput(attrs={'type': 'date'}),
              'payment_date': forms.DateInput(attrs={'type': 'date'}),
          }
        
    def __init__(self, *args, **kwargs):
        super(FeeHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,  # Adjust the number of rows
                'cols': 40,  # Adjust the number of columns
                'placeholder': 'Your Message',
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
       