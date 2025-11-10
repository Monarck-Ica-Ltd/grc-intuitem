#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciso_assistant.settings')
django.setup()

from iam.models import User

email = os.getenv('CISO_SUPERUSER_EMAIL', 'overseer@monarck.net')
password = os.getenv('TEMP_ADMIN_PASSWORD', 'ChangeMe123!')

try:
    if User.objects.filter(email=email).exists():
        print(f"✓ User {email} already exists")
        user = User.objects.get(email=email)
        # Update password in case it changed
        user.set_password(password)
        user.save()
        print(f"✓ Password updated for {email}")
    else:
        user = User.objects.create_superuser(
            email=email,
            password=password,
            first_name='System',
            last_name='Overseer'
        )
        print(f"✓ Superuser created: {email}")
except Exception as e:
    print(f"✗ Error: {e}")
