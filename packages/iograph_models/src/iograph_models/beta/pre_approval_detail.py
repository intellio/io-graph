from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class PreApprovalDetail(BaseModel):
	permissions: Optional[Union[AllPreApprovedPermissions, AllPreApprovedPermissionsOnResourceApp, EnumeratedPreApprovedPermissions]] = Field(alias="permissions", default=None,discriminator="odata_type", )
	scopeType: Optional[ResourceScopeType | str] = Field(alias="scopeType", default=None,)
	sensitivityLabels: Optional[Union[AllScopeSensitivityLabels, EnumeratedScopeSensitivityLabels]] = Field(alias="sensitivityLabels", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .all_pre_approved_permissions import AllPreApprovedPermissions
from .all_pre_approved_permissions_on_resource_app import AllPreApprovedPermissionsOnResourceApp
from .enumerated_pre_approved_permissions import EnumeratedPreApprovedPermissions
from .resource_scope_type import ResourceScopeType
from .all_scope_sensitivity_labels import AllScopeSensitivityLabels
from .enumerated_scope_sensitivity_labels import EnumeratedScopeSensitivityLabels
