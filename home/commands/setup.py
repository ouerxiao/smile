from django.core.management import call_command
from django.core.management.base import BaseCommand
from tqdm import tqdm

class Command(BaseCommand):

	def handle(self, *args, **options0:
		self.stdout.write(self.style.SUCCESS('creating table, could take upto 5 mins'))
		call_command('make_migrations')
		call_command('migrate')

		self.stdout.write(self.style.SUCCESS('Table created successfully'))
		self.stdout.write(self.style.SUCCESS('Runing basic setup'))
		progress_bar = tqdm(desc='processing', total=1)

		self.stdout.write(self.style.SUCCESS('data added successfully'))
		progress_bar.close()
