from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Profile, Post


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if not first_name:
            self.add_error('first_name', "First name is required.")
        if not last_name:
            self.add_error('last_name', "Last name is required.")

        if password != password_confirmation:
            self.add_error('password_confirmation', "Passwords do not match.")

        return cleaned_data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'category', 'cover_image']
        widgets = {
            'content': SummernoteWidget(attrs={
                'summernote': {
                    'toolbar': [
                        ['style', ['style']],
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['insert', ['link', 'picture']],
                    ],
                    'width': '100%',
                    'height': '300px',
                    'placeholder': 'Write your content here...',
                }
            }),
        }

def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or content.strip() == '':
            raise forms.ValidationError("Content is required.")
        return content

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 3,
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=username_or_email)
            username = user.username
        except User.DoesNotExist:
            username = username_or_email

        self.user_cache = authenticate(
            self.request,
            username=username,
            password=password,
        )
        if self.user_cache is None:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={
                    'username': self.username_field.verbose_name,
                },
            )

        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        max_length=30,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,  
        widget=forms.FileInput(attrs={'class': 'update-profile-input'})
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'update-bio-textarea',
            'maxlength': '150',
            'placeholder': 'Write something about yourself...'
        })
    )

    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'location']


class DeleteAccountForm(forms.Form):
    confirm = forms.BooleanField(
        label="I confirm that I want to delete my account."
    )


class SearchForm(forms.Form):
    query = forms.CharField(
        label="Search",
        max_length=100,
        required=False
    )
