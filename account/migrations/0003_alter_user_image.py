# Generated by Django 4.1.1 on 2022-09-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='Customer/2022/09/09/default-avatar-profile-icon-vector-social-media-user-photo-183042379.jpg', upload_to='Customers/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
