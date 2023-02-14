
from .models import Comment
from django import forms 

# 클래스 만들기
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
