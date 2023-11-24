from django.contrib.auth.management.commands import createsuperuser
from django.core.management.base import CommandError
from apps.accounts.models import UserAccount  # Import your custom user model

class Command(createsuperuser.Command):
    help = "Create a superuser with both email and username"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--email",
            dest="email",
            required=True,
            help="The email for the superuser",
        )
        parser.add_argument(
            "--username",
            dest="username",
            required=True,
            help="The username for the superuser",
        )

    def handle(self, *args, **options):
        email = options.get("email")
        username = options.get("username")

        if UserAccount.objects.filter(email=email).exists() or UserAccount.objects.filter(username=username).exists():
            raise CommandError("A user with this email or username already exists.")

        options["email"] = email
        options["username"] = username

        super().handle(*args, **options)
