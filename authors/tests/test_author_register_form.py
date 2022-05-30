from authors.forms import RegisterForm
from django.test import TestCase
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    #AO INVÉS DE CRIAR UM TESTE PARA CADA ITEM DO PLACEHOLDER, 
    #O PARAMETERIZED CRIA UMA LISTA
    #COM O CAMPO E O VALOR QUE DESEJA PASSAR PARA DENTRO DO TESTE
    #E JÁ VAI CHECANDO TODOS OS CAMPOS DE UMA ÚNICA VEZ
    @parameterized.expand([
        ('username','Your username'),
        ('first_name','Ex.: John'),
        ('last_name','Ex.: Doe'),
        ('email','Your e-mail'),
        ('password','Ex.: Type your password'),
        ('password2','Ex.: Repeat your password'),
    ])    
    def test_fields_placeholder_are_correct(self,field,placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)


    @parameterized.expand([
        ('username',
            'Obrigatório. 150 caracteres ou menos. '
            'Letras, números e @/./+/-/_ apenas.'),
        ('email','The e-mail must be valid.'),
        ('password','Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'),
    ])
    def test_fields_help_text_are_correct(self,field,needed):
        form = RegisterForm()
        current_help_text = form[field].field.help_text
        self.assertEqual(current_help_text, needed)



    @parameterized.expand([
        ('username','Username'),
        ('first_name','First name'),
        ('last_name','Last name'),
        ('email','E-mail'),
        ('password','Password'),
        ('password2','Password2'),
    ])
    def test_fields_labels_are_correct(self,field,needed):
        form = RegisterForm()
        current_label = form[field].field.label
        self.assertEqual(current_label, needed)
