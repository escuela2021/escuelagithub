from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroConMail(UserCreationForm):
	email = forms.EmailField(required=True, help_text='Campo requerido y debe ser valido, hasta 254 caracteres como maximo')

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('El email ya existe, ingresa uno nuevo')
		return email

from .models import perfil

LISTA_SEXOS = (('F','Femenino'),
		('M','Masculino'))

from django.core.exceptions import ValidationError

class PerfilForm(forms.ModelForm):


	class Meta:
		model = perfil
		fields = ('nombre','avatar','biografia','recibemails','sexo','nacimiento')

		widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'}),
			   'avatar':forms.ClearableFileInput(attrs={'class':'form-control'}),
			   'biografia': forms.Textarea(attrs={'class':'form-control'}),
			   'recibemails':forms.CheckboxInput(),
			   'sexo': forms.RadioSelect(choices=LISTA_SEXOS),
			   'nacimiento': forms.DateTimeInput(attrs={'class':'form-control'}),
			   	}

		labels = {'nombre':'Nombre',
				'avatar':'Logo',
				'biografia':'Experiencia',
				'recibemails': 'Puede recibir eMails',
				'sexo': 'Sexo',
				'nacimiento': 'Fecha de nacimiento'
				}


	def clean(self):
		data = self.cleaned_data
		nombre = data.get('nombre')
		biografia = data.get('biografia')
		if nombre != "Hola"or  biografia != "Como estas":
			raise ValidationError('El nombre debe ser Hola y la biografia como estas')
