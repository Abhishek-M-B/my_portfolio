import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

User = get_user_model()
username = os.getenv('ADMIN_USERNAME', 'Abhishek_MB')
email = os.getenv('ADMIN_EMAIL', 'Abhishekmbinfo@gmail.com')
password = os.getenv('ADMIN_PASSWORD', 'Abhishek@123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser {username} created successfully!")
else:
    print(f"Superuser {username} already exists.")