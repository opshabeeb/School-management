from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .forms import ContactForm, UserForm, LoginForm,UpdateUserForm,StudentForm,UpdateBookForm,AddLibraryHistoryForm,FeeHistoryForm
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class RoleRequiredMixin(UserPassesTestMixin):
    allowed_roles = []  # Define allowed roles for the view

    def test_func(self):
        user = self.request.user
        return user.is_superuser or (hasattr(user, 'role') and user.role in self.allowed_roles)

    def handle_no_permission(self):
        return redirect('login') 

class HomeView(TemplateView,LoginRequiredMixin):
    template_name = "Home.html"


class LoginView(View):
    template_name = 'registration/login.html'
    
    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, "Invalid username or password")
        return render(request, self.template_name, {'form': form})

class SignupView(View):
    template_name = 'registration/signup.html'
    
    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})
    

# admin 

class AdminDashborad(RoleRequiredMixin,TemplateView):
    template_name='admin/Dashboard.html'
    allowed_roles=['admin']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()  
        context['students'] = Student.objects.all()  
        return context
    
    
class UserCreateView(RoleRequiredMixin,CreateView):
    model=User
    form_class=UserForm
    template_name='admin/CreateUser.html'
    success_url= reverse_lazy('admindashboard')
    allowed_roles=['admin']
    
class UserUpdateView(RoleRequiredMixin,UpdateView):
    model=User
    form_class=UpdateUserForm
    template_name='admin/UpdateUser.html'
    success_url=reverse_lazy('admindashboard')
    context_object_name = 'user'
    allowed_roles=['admin']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()  
        return context
    
class UserDeleteView(RoleRequiredMixin,DeleteView):
    model = User
    template_name = 'admin/DeleteUser.html'  
    success_url = reverse_lazy('admindashboard') 
    allowed_roles=['admin'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_to_delete'] = self.object
        return context


class  CreateStudentView(RoleRequiredMixin,CreateView):
    model=Student
    form_class=StudentForm
    template_name='students/CreateStudent.html'
    success_url=reverse_lazy('admindashboard')
    allowed_roles=['admin']
    
class UpdateStudentView(RoleRequiredMixin,UpdateView):
    model=Student
    form_class=StudentForm
    template_name='students/UpdateStudent.html'
    success_url=reverse_lazy('admindashboard')
    allowed_roles=['admin']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = self.get_object()  
        return context
    
class StudentDeleteView(RoleRequiredMixin,DeleteView):
    model = Student
    template_name = 'students/DeleteStudent.html'  
    success_url = reverse_lazy('admindashboard')  
    allowed_roles=['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_to_delete'] = self.object
        return context

class LibraryHistoryView(RoleRequiredMixin,TemplateView):
    template_name="library/history_table.html"
    allowed_roles=['admin','librarian']
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["l_history"] =LibraryHistory.objects.all() 
        return context
    
    
    
class BookView(RoleRequiredMixin,TemplateView):
    template_name="library/book_table.html"
    allowed_roles=['admin','librarian']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()    
        return context


class AddBookView(RoleRequiredMixin,View):
    allowed_roles=['admin','librarian']
    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publication_date = request.POST.get('publication_date')
        available_copies = request.POST.get('available_copies')

       
        Book.objects.create(
            title=title,
            author=author,
            category=category,
            publication_date=publication_date,
            available_copies=available_copies
        )
        return redirect('booktable')
    
    

class UpdateBookView(RoleRequiredMixin,UpdateView):
    model = Book
    form_class = UpdateBookForm
    template_name = "library/editbook.html"
    success_url = reverse_lazy('booktable')  # Ensure 'booktable' URL name is correctly configured
    allowed_roles=['admin','librarian']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = self.get_object()  # Fetch the current book object being edited
        return context
class  DeleteBookView(RoleRequiredMixin,DeleteView):
    model=Book
    template_name="library/deletebook.html"
    success_url=reverse_lazy('booktable')
    allowed_roles=['admin','librarian']
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["book_to_delete"] = self.object
        return context

class AddLibraryHistoryView(RoleRequiredMixin,CreateView):
    model=LibraryHistory
    form_class=AddLibraryHistoryForm
    template_name='library/addhistory.html'
    success_url=reverse_lazy('libraryhistory')
    allowed_roles=['admin','librarian']
    
class MarkAsReturnedView(View):
    def post(self, request, pk):
        history_entry = get_object_or_404(LibraryHistory, pk=pk)
        history_entry.mark_as_returned()
        return redirect('libraryhistory')
    
class UpdateLibraryHistoryView(RoleRequiredMixin,UpdateView):
    model=LibraryHistory
    form_class=AddLibraryHistoryForm
    template_name='library/edithistory.html'
    success_url=reverse_lazy('libraryhistory')
    allowed_roles=['admin','librarian']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library_history"] = self.get_object()
        return context


class DeleteLibraryHistoryView(RoleRequiredMixin,DeleteView):
    model=LibraryHistory
    success_url=reverse_lazy('libraryhistory')
    template_name='library/deletehistory.html'
    allowed_roles=['admin','librarian']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history_to_delete"] = self.object 
        return context

class FeeHistoryTableView(RoleRequiredMixin,TemplateView):
    template_name='feehistory/HistoryTable.html'
    allowed_roles=['staff','admin']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fee_history"] = FeeHistory.objects.all()
        return context
    

class AddFeeHistory(RoleRequiredMixin,CreateView):
    model=FeeHistory
    form_class=FeeHistoryForm
    template_name='feehistory/AddFeeHistory.html'
    success_url=reverse_lazy('feehistory')
    allowed_roles=['staff','admin']
    
class MarkAsPaidView(View):
    def post(self, request, pk):
        history_entry = get_object_or_404(FeeHistory, pk=pk)
        history_entry.mark_as_paid()
        return redirect('feehistory')
    
    
class UpdateFeeHistoryView(RoleRequiredMixin,UpdateView):
    model=FeeHistory
    form_class=FeeHistoryForm
    template_name='feehistory/EditFeeHistory.html'
    success_url=reverse_lazy('feehistory')
    allowed_roles=['staff','admin']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fee_history"] = self.get_object() 
        return context


class DeleteFeeHistoryView(RoleRequiredMixin,DeleteView):
    model=FeeHistory
    template_name='feehistory/DeleteFeeHistory.html'
    success_url=reverse_lazy('feehistory')
    allowed_roles=['staff','admin']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history_to_delete"] = self.object
        return context
    

class StaffDashboardView(RoleRequiredMixin,TemplateView):
    template_name='staff/dashboard.html'
    allowed_roles=['staff']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = LibraryHistory.objects.all()  
        context['students'] = Student.objects.all()  
        return context
    
class LibrarianDashboardView(RoleRequiredMixin,TemplateView):
    template_name='librarian/dashboard.html'
    allowed_roles=['librarian']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fee_history'] = FeeHistory.objects.all()  
        context['students'] = Student.objects.all()  
        return context
    


class  StaffCreateStudentView(RoleRequiredMixin,CreateView):
    model=Student
    form_class=StudentForm
    template_name='students/CreateStudent.html'
    success_url=reverse_lazy('staff_dashboard')
    allowed_roles=['staff']
    
class StaffUpdateStudentView(RoleRequiredMixin,UpdateView):
    model=Student
    form_class=StudentForm
    template_name='students/UpdateStudent.html'
    success_url=reverse_lazy('staff_dashboard')
    allowed_roles=['staff']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = self.get_object()  
        return context
    
class StaffStudentDeleteView(RoleRequiredMixin,DeleteView):
    model = Student
    template_name = 'students/DeleteStudent.html'  
    success_url = reverse_lazy('staff_dashboard')  
    allowed_roles=['staff']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_to_delete'] = self.object
        return context


class ContactUs(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)