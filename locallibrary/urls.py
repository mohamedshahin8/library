"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from catalog import views


urlpatterns = [
    url(r'^home/$', views.home , name='home'),
    url(r'^home/books/$', views.BookListView.as_view() , name='books'),
    url(r'^home/books/(?P<pk>\d+)$', views.BookDetailView.as_view() , name='book_detail'),
    url(r'^home/authors/$', views.AuthorListView.as_view() , name='authors'),
    url(r'^home/authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view() , name='author_detail'),
    url(r'^home/mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^home/books/(?P<pk>\d+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
