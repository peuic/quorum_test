import csv
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Load data from a CSV file into a specified model'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model names to be imported')
        parser.add_argument('csv_file', type=str, help='Path to CSV')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        csv_file = kwargs['csv_file']

        try:
            # Obtém o modelo dinamicamente
            model = apps.get_model('core', model_name)
        except LookupError:
            self.stderr.write(self.style.ERROR(f"Model '{model_name}' not found."))
            return

        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Cria ou atualiza os registros no banco de dados
                    obj, created = model.objects.update_or_create(
                        id=row['id'],  # Assume que todos os modelos têm um campo 'id'
                        defaults=row
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"{model_name} with ID {obj.id} created."))
                    else:
                        self.stdout.write(self.style.WARNING(f"{model_name} with ID {obj.id} updated."))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File '{csv_file}' not found."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing data: {str(e)}"))