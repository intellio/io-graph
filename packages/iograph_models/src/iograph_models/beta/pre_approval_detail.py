from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PreApprovalDetail(BaseModel):
	permissions: SerializeAsAny[Optional[PreApprovedPermissions]] = Field(alias="permissions",default=None,)
	scopeType: Optional[ResourceScopeType | str] = Field(alias="scopeType",default=None,)
	sensitivityLabels: SerializeAsAny[Optional[ScopeSensitivityLabels]] = Field(alias="sensitivityLabels",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .pre_approved_permissions import PreApprovedPermissions
from .resource_scope_type import ResourceScopeType
from .scope_sensitivity_labels import ScopeSensitivityLabels

