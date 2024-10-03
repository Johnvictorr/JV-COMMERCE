from django import forms
from .models import Produto, Cliente, Compras


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'preco', 'peso', 'foto']
        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 
                                           'placeholder': 'Nome do Produto',
                                           'style': 'font-family: verdana, sans-serif;'}),


            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 
                                                   'placeholder': 'Quantidade do Produto',
                                                   'style': 'font-family: verdana, sans-serif;'}),


            'preco': forms.NumberInput(attrs={'class': 'form-control', 
                                              'placeholder': 'R$',
                                              'style': 'font-family: verdana, sans-serif;'}),


            'peso': forms.NumberInput(attrs={'class': 'form-control', 
                                             'placeholder': 'Kg',
                                             'style': 'font-family: verdana, sans-serif;'}),


            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'})

            }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone']
        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 
                                            'placeholder': 'Nome',
                                            'style': 'font-family: verdana, sans-serif;'}),


            'cpf': forms.TextInput(attrs={'class': 'form-control', 
                                            'placeholder': 'CPF',
                                            'style': 'font-family: verdana, sans-serif;',
                                            'maxlength': '11'}),


            'telefone': forms.TextInput(attrs={'class': 'form-control', 
                                                'placeholder': 'Telefone',
                                                'style': 'font-family: verdana, sans-serif;',
                                                'maxlength': '15'})

            }


class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['cliente', 'valorPago', 'pagamento', 'produtoComprado', 'quantidadeProdutos']
        widgets = {

            'cliente': forms.Select(attrs={'class': 'form-control', 
                                              'placeholder': 'Cliente',
                                              'style': 'font-family: verdana, sans-serif;'}),


            'valorPago': forms.NumberInput(attrs={'class': 'form-control', 
                                                  'placeholder': 'Valor Pago',
                                                  'style': 'font-family: verdana, sans-serif;',
                                                  'step': '0.01'}),


            'pagamento': forms.CheckboxInput(attrs={'class': 'form-check-input', 
                                                    'style': 'margin-left: 10px;'}),


            'produtoComprado': forms.Select(attrs={'class': 'form-control', 
                                                   'style': 'font-family: verdana, sans-serif;'}),


            'quantidadeProdutos': forms.NumberInput(attrs={'class': 'form-control', 
                                                           'placeholder': 'Quantidade de Produtos',
                                                           'style': 'font-family: verdana, sans-serif;',
                                                           'min': '1'})
            }