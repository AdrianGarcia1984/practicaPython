from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label="title of task", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description=forms.CharField(label="description of task",widget=forms.Textarea( attrs={'class':'input'}))

class createNewProject(forms.Form):
    name = forms.CharField(label="name of project", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
   