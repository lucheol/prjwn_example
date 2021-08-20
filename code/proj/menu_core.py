from django.urls import reverse
from django.utils.translation import gettext as _


class MenuObject:
    def __init__(self, order, slug, title, url='None', icon='fa-circle-o', visible=True, iframe=False, has_help=False, extra_info=None):
        self.order = order
        self.slug = slug
        self.title = title
        self.url = url
        self.icon = icon
        self.visible = visible
        self.iframe = iframe
        self.has_help = has_help
        self.extra_info = extra_info or {}


BASE_MENU = [

    MenuObject(order=99, slug='profile.*', title=_("Profile"), url=reverse("dashboard-profile"), visible=False),
    MenuObject(order=9901, slug='profile.user.*', title=_("User"), icon='fa-user'),
    MenuObject(order=990101, slug='profile.user.personal_info', title=_("Personal Info"), url=reverse("profile-personal-info"), icon='fa-user'),
    MenuObject(order=990101, slug='profile.user.password', title=_("Change Password"), url=reverse("profile-password-change"), icon='fa-key'),
    MenuObject(order=990102, slug='profile.user.password_done', title=_("Change Password Done"), url=reverse("profile-password-done"), icon='fa-key', visible=False),
    MenuObject(order=990103, slug='profile.user.avatar', title=_("Avatar"), url=reverse("profile-avatar-update"), icon='fa-camera'),

    MenuObject(order=99, slug='config.*', title=_("Configuration"), url=reverse("dashboard-config")),
    MenuObject(order=9902, slug='config.audit.*', title=_("Audit"), icon='fa-user-secret'),
    MenuObject(order=990201, slug='config.audit.log', title=_("Audit log"), url=reverse("audit-log-list"), icon='fa-database', has_help=False),
    MenuObject(order=9903, slug='config.users.*', title=_("User and authorization"), icon="fa-users"),
    MenuObject(order=32, slug='config.users.users', title=_("Users"), url=reverse('users-list'), icon="fa-user"),
    MenuObject(order=9903, slug='config.users.roles', title=_("Roles"), url=reverse("users-role-list"), icon="fa-lock"),

]