from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home',HomeView.as_view(),name='home'),
    path('',LoginView.as_view(),name='login'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
    
    path('admin_dashboard/',AdminDashborad.as_view(),name='admindashboard'),
    path('usercreate',UserCreateView.as_view(),name='createuser'),
    path('users/edit/<int:pk>/', UserUpdateView.as_view(), name='updateuser'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='deleteuser'),
    
    path('add-student/', CreateStudentView.as_view(), name='add_student'),
    path('student/edit/<int:pk>/', UpdateStudentView.as_view(), name='update_student'),
    path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    
    
    path('libraryhistory',LibraryHistoryView.as_view(),name='libraryhistory'),
    path('books',BookView.as_view(),name='booktable'),
    path('addbook',AddBookView.as_view(),name='addbook'),
    path('editbook/<int:pk>/',UpdateBookView.as_view(),name='editbook'),
    path('deletebook/<int:pk>/',DeleteBookView.as_view(),name='deletebook'),
    
    
    path('add_libraryhistory/',AddLibraryHistoryView.as_view(),name='add_library'),
    path('mark_as_returned/<int:pk>/', MarkAsReturnedView.as_view(), name='mark_as_returned'),
    path('update_libraryhistory/<int:pk>/', UpdateLibraryHistoryView.as_view(), name='update_history'),
    path('delete_libraryhistory/<int:pk>/', DeleteLibraryHistoryView.as_view(), name='delete_history'),
    
    
    path('feehistory', FeeHistoryTableView.as_view(), name='feehistory'),
    path('addfeehistory', AddFeeHistory.as_view(), name='add_feehistory'),
    path('markpaid/<int:pk>/', MarkAsPaidView.as_view(), name='markpaid'),
    path('edit_feehistory/<int:pk>/', UpdateFeeHistoryView.as_view(), name='edit_fee'),
    path('delete_feehistory/<int:pk>/', DeleteFeeHistoryView.as_view(), name='delete_fee'),
    
    
    path('staff_dashboard/', StaffDashboardView.as_view(), name='staff_dashboard'),
    path('staff_add-student/', StaffCreateStudentView.as_view(), name='staff_add_student'),
    path('staff_student/edit/<int:pk>/', StaffUpdateStudentView.as_view(), name='staff_update_student'),
    path('Staff_student/delete/<int:pk>/', StaffStudentDeleteView.as_view(), name='staff_delete_student'),
    
    
    path('librarian_dashboard/', LibrarianDashboardView.as_view(), name='librarian_dashboard'),
    
    
    path('Contactus/', ContactUs.as_view(), name='Contact'),
    
    
    
    


    
    
    

    
    
    
]