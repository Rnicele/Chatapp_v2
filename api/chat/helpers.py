from rest_framework.authtoken.models import Token


def user_construct(user):
    fields = ['id', 'email', 'first_name', 'last_name', 'date_joined']
    token, created = Token.objects.get_or_create(user=user)

    return {
        'user': {field: getattr(user, field) for field in fields},
        'token': token.key
    }
