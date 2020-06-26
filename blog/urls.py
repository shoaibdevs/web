from django.urls import path
from blog.views import data_views, show_views, edit_views, update_views, delete_views, panel_views,\
signup_views, user_show, login_views, logout_views


urlpatterns = [
	
	path('create/', data_views, name = 'data'),
	path('table/', show_views, name = 'table'),
	path('edit/<int:id>/', edit_views, name = 'edit'),
	path('update/<int:id>/', update_views, name = 'update'),
	path('delete/<int:id>/', delete_views, name = 'delete'),
	path('panel/', panel_views, name = 'panel'),
	path('signup/', signup_views, name = 'signup'),
	path('user/', user_show, name = 'user-show'),
	path('login/', login_views, name="login"),
	path('logout/', logout_views, name='logout'),

]