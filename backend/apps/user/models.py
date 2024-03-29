from django.db import models

# Create your models here.
class User (models.Model) :
    class Meta (object) :
        db_table = "user"

    user_name = models.CharField (
        "user Name", blank=False, null=False, max_length=50, db_index=True
    )
    password = models.CharField (
        "Password", blank=False, null=False, max_length=50, db_index=True
    )
    email = models.EmailField (
        "email", blank=False, null=False, max_length=250, db_index=True
    )
    token = models.CharField (
        "Token", blank=True, null=True, max_length=500, db_index=True
    )
    token_expires_at = models.DateTimeField (
        "Token Expires At", blank=True, null=True
    )
    created_at = models.DateTimeField (
        "Created Datetime", blank=True, null=True, auto_now_add=True
    )
    updated_at = models.DateTimeField (
        "Updated Datetime", blank=True, null=True, auto_now=True
    )