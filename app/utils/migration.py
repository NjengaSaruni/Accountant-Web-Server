import os
import csv

import django
from django.utils import timezone
import csv
import os
import pytz

import django
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()
from app.accounts.models import User

from app.finance.models import Tag, Transaction

if __name__ == '__main__':
    user = User.objects.get(email='peternjengask@gmail.com')

    with open('transactions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        current_tz = timezone.get_current_timezone()
        Transaction.objects.all().delete()
        for row in csv_reader:
            try:
                date = pytz.utc.localize(timezone.datetime.strptime(row[0], '%Y-%m-%d'))
                description = row[1]
                amount = float(row[3])
                tag = row[5]
                tag = Tag.objects.get(
                    name=tag.lower(),
                    created_by=user,
                )

                transaction = Transaction.objects.create(
                    amount=amount,
                    tag=tag,
                    created_at=date,
                    created_by=user,
                    description=description,
                    transaction_date=date
                )
                transaction.created_at = date
                transaction.transaction_date = date
                transaction.save()

                print(transaction)
            except Exception:
                pass