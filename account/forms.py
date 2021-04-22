from django import forms
from django.contrib.auth.forms import AuthenticationForm # ユーザー認証のためのクラス／ユーザー登録のためのクラス／パスワード変更のためのクラス
from django.contrib.auth import get_user_model # ユーザーモデルを取得するため


# ユーザーモデル取得
User = get_user_model()


'''ログイン用フォーム'''
class LoginForm(AuthenticationForm):

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる