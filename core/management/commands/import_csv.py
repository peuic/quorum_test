import csv
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o modelo especificado'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Nome do modelo para o qual os dados serão importados')
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        csv_file = kwargs['csv_file']

        try:
            # Obtém o modelo dinamicamente
            model = apps.get_model('core', model_name)
        except LookupError:
            self.stderr.write(self.style.ERROR(f"Modelo '{model_name}' não encontrado."))
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
                        self.stdout.write(self.style.SUCCESS(f"{model_name} com ID {obj.id} criado."))
                    else:
                        self.stdout.write(self.style.WARNING(f"{model_name} com ID {obj.id} atualizado."))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"Arquivo '{csv_file}' não encontrado."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao importar dados: {str(e)}"))