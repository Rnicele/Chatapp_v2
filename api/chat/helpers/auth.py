from django.forms.models import model_to_dict


def user_construct(user):
    test = model_to_dict(user)
    fields = ['id', 'email', 'first_name', 'last_name', 'date_joined']
    return {'user': {field: test[field] for field in fields}}
