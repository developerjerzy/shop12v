from .models import Comment
from django import forms



class CommentForm(forms.ModelForm):
    """Класс отвечает за создание формы комментария

    Поля:
    Имя того кто пишет комментарии
    Емэйл
    Тело комметнария
    """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')