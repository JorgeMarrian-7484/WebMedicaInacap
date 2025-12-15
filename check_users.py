#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicWeb.settings')
django.setup()

from django.contrib.auth.models import User, Group

# Contar usuarios
users_count = User.objects.count()
print(f"Total de usuarios: {users_count}\n")

# Listar usuarios
users = User.objects.all()[:10]
for u in users:
    print(f"  - {u.username} (id: {u.id}, email: {u.email})")

# Contar grupos
groups = Group.objects.all()
print(f"\nGrupos registrados: {groups.count()}")
for g in groups:
    print(f"  - {g.name} ({g.user_set.count()} usuarios)")
