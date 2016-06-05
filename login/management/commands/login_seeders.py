from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'This command will seed the database (Users and types)'

    def handle(self, *args, **options):
        print('\n  Users Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        User.objects.all().delete()
        Group.objects.all().delete()
        Permission.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        user1 = User.objects.create_user(username='usuario', password='1111')
        user2 = User.objects.create_user(username='administrador', password='1111')
        user3 = User.objects.create_user(username='bungalow', password='1111')
        user4 = User.objects.create_user(username='evento', password='1111')
        user5 = User.objects.create_user(username='cancha', password='1111')
        user6 = User.objects.create_user(username='cajero', password='1111')
        user7 = User.objects.create_user(username='membresia', password='1111')
        user8 = User.objects.create_user(username='empresa', password='1111')

        usuario = Group.objects.create(name='usuarios')
        admin = Group.objects.create(name='admins')
        bungalows = Group.objects.create(name='bungalows')
        eventos = Group.objects.create(name='eventos')
        canchas = Group.objects.create(name='canchas')
        cajero = Group.objects.create(name='cajeros')
        membresia = Group.objects.create(name='membresias')
        empresa = Group.objects.create(name='empresas')

        usuario.user_set.add(user1)
        admin.user_set.add(user2)
        bungalows.user_set.add(user3)
        eventos.user_set.add(user4)
        canchas.user_set.add(user5)
        cajero.user_set.add(user6)
        membresia.user_set.add(user7)
        empresa.user_set.add(user8)

        content_type = ContentType.objects.create(app_label='dummy', model='unused')

        permission_usuario = Permission.objects.create(codename='permission_usuario', name='Can Do User Things', content_type=content_type)
        permission_admin = Permission.objects.create(codename='permission_admin', name='Can Do Admin Things', content_type=content_type)
        permission_bungalows = Permission.objects.create(codename='permission_bungalows', name='Can Do Bungalow Things', content_type=content_type)
        permission_eventos = Permission.objects.create(codename='permission_eventos', name='Can Do Event Things', content_type=content_type)
        permission_canchas = Permission.objects.create(codename='permission_canchas', name='Can Do Field Things', content_type=content_type)
        permission_cajero = Permission.objects.create(codename='permission_cajero', name='Can Do Cashier Things', content_type=content_type)
        permission_membresia = Permission.objects.create(codename='permission_membresia', name='Can Do Membership Things', content_type=content_type)
        permission_empresa = Permission.objects.create(codename='permission_empresa', name='Can Do Business Things', content_type=content_type)

        usuario.permissions.add(permission_usuario)  
        bungalows.permissions.add(permission_bungalows)
        eventos.permissions.add(permission_eventos)
        canchas.permissions.add(permission_canchas)
        cajero.permissions.add(permission_cajero)
        membresia.permissions.add(permission_membresia)
        empresa.permissions.add(permission_empresa)

        admin.permissions.add(permission_admin)
        admin.permissions.add(permission_usuario)
        admin.permissions.add(permission_bungalows)
        admin.permissions.add(permission_eventos)
        admin.permissions.add(permission_canchas)
        admin.permissions.add(permission_cajero)
        admin.permissions.add(permission_membresia)
        admin.permissions.add(permission_empresa)



        print('Data has been inserted\n')