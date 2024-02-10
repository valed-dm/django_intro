# django_intro
https://docs.djangoproject.com/en/5.0/intro/tutorial01/

### Первое приложение Django

- создание проекта
- создание приложения polls (опросы)
[<img src="mysite/images/ultimate_question.png" width="1000"/>]()

- urlpatterns: route, view, kwargs, name
- database setup, models
- создание admin user, superuser
- views, templates, render(), get_object_or_404()

углубился в вопрос race condition in Django (см. race_condition.py):
[<img src="mysite/images/race_condition.png" width="1000"/>]()

есть несколько вариантов решения:
с использованием F expression для инкремента значения:
[<img src="mysite/images/race_condition_solved.png" width="1000"/>]()

с использованием атомарных транзакций:

https://github.com/valed-dm/cookbook/blob/dev/recipes/views.py:
```python
with transaction.atomic():
        for ing in ingredients:
            "'F' expression avoids retrieving the 'times_used' value from the database into Python memory."
            "It performs the increment operation directly at the database level"
            Ingredient.objects.filter(id=ing.ingredient.id).update(times_used=F("times_used") + 1)
```

с использованием get_or_create(), update_or_create():

```python
updated_values = {"unit": unit, "qty": qty}

    obj, created = RecipeIngredient.objects.update_or_create(
        recipe=recipe, ingredient=ingredient,
        defaults=updated_values
    )
```

- forms
- generic views
- automated testing
- static files
- настройка admin form
[<img src="mysite/images/users.png" width="1000"/>]()
[<img src="mysite/images/questions.png" width="1000"/>]()
[<img src="mysite/images/change_question.png" width="1000"/>]()


- Django Debug Toolbar
[<img src="mysite/images/debug_toolbar.png" width="1000"/>]()


- создание пакета приложения
[<img src="mysite/images/django_polls_installed.png" width="1000"/>](mysite/images/django_polls_installed.png)