from django.db import models

class Offer(models.Model):
    bank_name = models.CharField(
        max_length=255,
        verbose_name='Наименование банка'
    )
    term_min = models.PositiveSmallIntegerField(
        default=3, # Минимальный срок как правило составляет 3 – 5 лет.
        verbose_name='Срок ипотеки, ОТ'
    )
    term_max = models.PositiveSmallIntegerField(
        default=30, # Максимальный срок, на сколько дается ипотека в России сегодня, составляет 30 лет.
        verbose_name='Срок ипотеки, ДО'
    )
    rate_min = models.FloatField(
        default=4.4, # Нашел минимальную ставку 4.4%
        verbose_name='Ставка, ОТ'
    )
    rate_max = models.FloatField(
        default=17.0,
        verbose_name='Ставка, ДО'
    )
    payment_min = models.PositiveIntegerField(
        verbose_name='Сумма кредита, ОТ'
    )
    payment_max = models.PositiveIntegerField(
        verbose_name='Сумма кредита, ДО'
    )

    class Meta:
        verbose_name = 'Предложения банка'
        verbose_name_plural = 'Предложения банка'

    def __str__(self):
        return self.bank_name
