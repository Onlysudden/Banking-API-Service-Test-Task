# Шаблон тестового задания

## Техническое задание

Необходимо было разработать калькулятор ипотечных предложений на основе [примера](https://www.sravni.ru/ipoteka/?mortgagePurpose=1&creditAmount=11849421&initialAmount=1500000&mortgageTerm=120).

[Пример API](https://documenter.getpostman.com/view/6802079/UVeAvonG) c образцами запросов который нужно реализовать

----

### Пользовательский сценарий
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек. Тип данных: integer
2. Первоначальный взнос, в рублях без копеек. Тип данных: integer
3. Срок, в годах. Тип данных: integer

В ответ ему приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
1. Наименование банка. Тип данных: string
2. Ипотечная ставка, в процентах. Тип данных: float
3. Платеж по ипотеке, в рублях без копеек.  Тип данных: integer

----

### Технические требования
Исходя из выше описанного пользовательского сценария, нужно:
1. Написать модель для хранения ипотечных предложений.
2. Написать ViewSet для реализации функционала CRUD ипотечных предложений.
3. Фильтрацию ипотечных предложений, по введенным параметрам.
4. Реализовать функционал, который будет рассчитывать платеж у всех валидных ипотечных предложений.
5. Сортировка ипотечных предложений по ставке(процент по ипотеке) и по платежу. 
6. Тесты для всего вышеперечилсенного.

----

### Используемый стек
1) Django. Обязательно
2) [DRF](https://www.django-rest-framework.org/). Обязательно
3) [django-filters](https://django-filter.readthedocs.io/en/stable/guide/usage.html). По желанию

----

#### Что сделано?

- [x] Модель для хранения ипотечных предложений, используемая база PostgreSQL.
- [x] ViewSet реализовывающий CRUD ипотечных предложений.
- [x] Фильтрация по входным данным год и сумма ипотеки, а также по дополнительным
параметрам таких ках минимальная и максимальная ставка.
- [x] Сериализатор для обработки ипотечных предложений, а также расчета месячного платежа.
- [x] Сортировка ипотечных предложений по ставке и по сумме ипотеки. 
- [x] Тесты покрывающие весь CRUD ипотечных предложений.