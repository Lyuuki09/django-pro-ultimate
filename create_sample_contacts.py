#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdev.settings')
django.setup()

from mycontacts.models import Contact

# Limpar contatos existentes
Contact.objects.all().delete()

# Criar contatos de exemplo baseados na imagem
contacts_data = [
    {
        'name': 'Johnny',
        'relation': 'Irmao',
        'phone': '87988989',
        'email': 'johnny@johnny'
    },
    {
        'name': 'Gabriel',
        'relation': 'asdasd',
        'phone': 'asdsad',
        'email': 'asdasd'
    },
    {
        'name': 'Anderson',
        'relation': 'Primo',
        'phone': '8768767',
        'email': 'and@and'
    }
]

# Criar os contatos
for contact_data in contacts_data:
    contact = Contact.objects.create(**contact_data)
    print(f"Contato criado: {contact.name}")

print(f"\nTotal de contatos criados: {Contact.objects.count()}")
print("Contatos criados com sucesso!")
