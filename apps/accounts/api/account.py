from orgs.mixins.api import OrgBulkModelViewSet
from rbac.permissions import SafeRolePermission
from .. import serializers
from ..models import Account
from ..utils import get_user_safes


__all__ = ['AccountViewSet']


class SafeViewSetMixin(object):
    model = None
    permission_classes = (SafeRolePermission, )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_permission_safes(queryset)
        return queryset

    def filter_permission_safes(self, queryset):
        safes = self.get_user_permission_safes()
        queryset = queryset.filter(safe__in=safes)
        return queryset

    def get_user_permission_safes(self):
        safes = get_user_safes(self.request.user)
        permission_safes = []
        for safe in safes:
            has_permission = SafeRolePermission.check_user_permission(
                self.request.user, safe, model=self.model, view_action=self.action
            )
            if not has_permission:
                continue
            permission_safes.append(safe)
        return permission_safes

    def perform_create(self, serializer):
        objs = self.get_to_create_objects(serializer)
        self.check_objects_permissions(objs)
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        objs = self.get_to_update_objects(serializer)
        self.check_objects_permissions(objs)
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        self.check_objects_permissions([instance])
        return super().perform_destroy(instance)

    def check_objects_permissions(self, objs):
        for obj in objs:
            self.check_object_permissions(self.request, obj)

    def get_to_create_objects(self, serializer):
        validated_data = serializer.validated_data
        if not isinstance(validated_data, list):
            validated_data = [validated_data]
        objs = [self.model(**data) for data in validated_data]
        return objs

    def get_to_update_objects(self, serializer):
        if isinstance(serializer.instance, self.model):
            objs = [serializer.instance]
        else:
            # bulk
            id_attr = getattr(serializer.child.Meta, 'update_lookup_field', 'id')
            objs_ids = [i.pop(id_attr) for i in serializer.validated_data]
            objs = serializer.instance.filter(**{'{}__in'.format(id_attr): objs_ids})
        return objs


class AccountViewSet(SafeViewSetMixin, OrgBulkModelViewSet):
    serializer_class = serializers.AccountSerializer
    model = Account
    filterset_fields = {
        'id': ['exact', 'in'],
        'name': ['exact'],
        'username': ['exact'],
        'type': ['exact', 'in'],
        'type__name': ['exact', 'in'],
        'address': ['exact'],
        'is_privileged': ['exact'],
        'safe': ['exact', 'in'],
        'safe__name': ['exact']
    }
    search_fields = (
        'id', 'name', 'username', 'type', 'type__name', 'address', 'is_privileged', 'safe',
        'safe__name'
    )
