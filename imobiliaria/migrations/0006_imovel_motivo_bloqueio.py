from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imobiliaria', '0005_locacao_motivo_cancelamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='motivo_bloqueio',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
