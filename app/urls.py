from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Index, name="index"),
    

    # page rendering
    path("signup/", views.SignupPage, name="signup"),
    # path("search/", views.SearchPage, name="search"),
    path("contact/", views.ContactPage, name="contact"),
    path("postcard/", views.PostCardPage, name="postcard"),
    path("showcard/", views.ProductCard, name="showcard"),
    path("register/", views.Register, name="register"),  # type: ignore
    path("otppage/", views.OTPPage, name="otppage"),
    path("queryPage/", views.QueryPage, name="queryPage"),
    path("product/", views.ProductPage, name="product"),
    path("login", views.LoginPage, name="login"),
    path("detail_view/<int:pk>", views.DetailView, name="detail_view"),  # type: ignore

    # Actual internal processes
    path("otp/", views.OTPVerify, name="otp"),
    path("login/", views.LoginUser, name="login"),  # type: ignore
    path("logout/", views.Logout, name="logout"),  # type: ignore
    path("showdata/", views.ShowProductData, name="showdata"),
    path("already/", views.AlreadyLogout, name="already"),
    path("queries/", views.Queries, name="queries"),  # type: ignore
    # path("Detailprocess/", views.Detailprocess, name="Detailprocess")  # type: ignore
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
