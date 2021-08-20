from django.urls import path, include
from .apis import CeleryTaskStatusAPI, MenuHelpAPI
from .views import AuditLogList, DashboardIndexView
from .decorators import register_resource
from django.utils.translation import gettext as _

urlpatterns = [
    path('admin/maintenance-mode/', include('maintenance_mode.urls')),
    path('', include('switchblade_users.urls')),

    path('', register_resource(DashboardIndexView.as_view(page_title='Dashboard', header='Dashboard', columns=[3, 3, 3, 3])), name='dashboard-index'),

    path('config/', include([
        path('', register_resource(DashboardIndexView.as_view(page_title=_('Configuration'), header=_('Configuration'), columns=[3, 3, 3, 3])), name='dashboard-config'),
        path('audit-log/', register_resource(AuditLogList), name='audit-log-list'),
    ])),

    path('api/', include([
        path('async-task-status/', CeleryTaskStatusAPI.as_view(), name='api-async-task-status'),
        path('help-text/', MenuHelpAPI.as_view(), name='api-help-text'),
    ])),


]

