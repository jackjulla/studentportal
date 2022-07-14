from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name ="notes"),
    path('delete_note/<int:pk>',views.delete_note,name ="note"),
    path('notes_detail/<int:pk>',views.NotesDetailView(),name ="notes-detail"),

    path ('homework',views.homework,name ="homework"),
    path ('update_homework/<int:pk>',views.update_homework,name ="homework"),
    path ('delete_homework/int:pk',views.delete_homework,name ="delete-homework"),

    path ('youtube',views.youtube,name="youtube"),

    path ('todo',views.todo,name="todo"),
    path ('update_todo/<int:pk>',views.update_todo,name ="update-todo"),
    path ('delete_todo/<int:pk>',views.delete_todo,name ="delete-todo"),

    path ('books',views.books,name="books"),

    path ('dictionary',dictionary,name="dictionary"),

    path ('wiki',views.wiki,name="wiki"),

    path ('conversion',views.conversion,name="conversion"),
]
