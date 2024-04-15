from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field


class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request=request, user=user, form=form, commit=False)

        data = form.cleaned_data
        initials = data.get("initials")
        if initials:
            user_field(user, "initials", initials)

        self.populate_username(request, user)
        if commit:
            user.save()
        return user
