from .forms import LoginForm, SignupForm
from django.contrib.auth import get_user_model # ユーザーモデルの取得
from django.contrib.auth.mixins import UserPassesTestMixin 
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views import generic


'''ユーザーモデルの取得'''
User = get_user_model()

'''トップページ'''
class TopView(generic.TemplateView):
    template_name = 'account/top.html'


'''ログイン'''
class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'


'''ログアウト'''
class Logout(LogoutView):
    template_name = 'account/logout_done.html'


'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        # 参考：スーパーユーザーも許可することができる
        user = self.request.user
        return user.pk == self.kwargs['pk'] # or user.is_superuser


'''マイページ'''
class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'account/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される


'''サインアップ'''
class Signup(generic.CreateView):
    template_name = 'account/user_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('account:signup_done')
    
    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''
class SignupDone(generic.TemplateView):
    template_name = 'account/signup_done.html'