from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
    	model = Question
    	fields = ("title", "text")

    def save(self, commit=True):
    	question = super(QuestionForm, self).save(commit=False)
        question.title = self.cleaned_data["title"]
        question.text = self.cleaned_data['text']
        if commit:
            question.save()
        return question

class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
    	model = Answer
    	fields = ('text',)

    def save(self, commit=True):
    	answer = super(QuestionForm, self).save(commit=False)
        answer.text = self.cleaned_data['text']
        if commit:
            answer.save()
        return answer
