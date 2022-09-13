from rest_framework import serializers

from .models import Offer

class OfferSerializer(serializers.ModelSerializer):
    """Сериализатор / десериализатор для данных модели для всей обработки запросов: GET, POST, PATCH, DEL"""

    payment = serializers.SerializerMethodField(method_name='get_payment', read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'payment', 'bank_name', 'term_min',
                  'term_max', 'rate_min', 'rate_max', 'payment_min', 'payment_max']
    
    def get_payment(self, obj):
        """Функция проверки входных данных для расчета месячного платежа"""

        try:
            request = self.context.get('request')
            price = request.query_params.get('price', None)
            deposit = request.query_params.get('deposit', None)
            term = request.query_params.get('term', None)

            if request.method in ('GET', 'PATCH'):
                if not price or not deposit or not term:
                    return 0
                if (price == 0 or deposit == 0 or term == 0):
                    return 0
                return self.payment_calculate(obj)
            else:
                return 0
        except ValueError:
            raise 'Could not convert data to an integer.'
        except BaseException as error:
            raise f'Unexpected {error}, {type(error)}'
    

    def payment_calculate(self, obj):
        """Функция для расчета ежемесячного платежа"""

        request = self.context.get('request')
        price = request.query_params.get('price')
        deposit = request.query_params.get('deposit')
        term = request.query_params.get('term')
        
        """Формула для расчета суммы ежемесячных аннуитетных платежей
        Ссылка - https://www.raiffeisen.ru/wiki/formuly-dlya-samostoyatelnogo-rascheta-ipoteki/
        Для значения ставки просто взял rate_min для облегчения расчетов"""
        
        real_price = int(price) * (100 - int(deposit)) / 100

        payment = int(round(real_price * (obj.rate_min / 0.12) / (1 - (1 + obj.rate_min / 0.12) * (1 - int(term) * 12))))
        
        return payment




