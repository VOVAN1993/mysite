from django.contrib.sites.models import Site, RequestSite
from django.template.loader import render_to_string
from registration.models import RegistrationProfile
from registration.views import RegistrationView
from mysite import settings
from novajoy.models import Account, PostLetters


class RegBackend(RegistrationView):
    def register(self, request, **kwargs):
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        user = Account.objects.create_user(username, email, password)
        user.is_active = False
        user.save()
        profile = RegistrationProfile.objects.create_profile(user)
        ctx_dict = {'activation_key': profile.activation_key,
                    'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': site}
        subject = render_to_string('registration/activation_email_subject.txt',
                                   ctx_dict)
        subject = ''.join(subject.splitlines())
        # write message for DB PostLetters
        message = render_to_string('registration/activation_email.txt',
                                   ctx_dict).__str__()
        post_letters = PostLetters(target=profile.user.email, title=subject, body=message)
        post_letters.save()
        return profile

    def get_success_url(self, request=None, user=None):
        return "/accounts/register/complete"

