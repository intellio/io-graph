from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionGrantConditionSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientApplicationIds: Optional[list[str]] = Field(default=None,alias="clientApplicationIds",)
	clientApplicationPublisherIds: Optional[list[str]] = Field(default=None,alias="clientApplicationPublisherIds",)
	clientApplicationsFromVerifiedPublisherOnly: Optional[bool] = Field(default=None,alias="clientApplicationsFromVerifiedPublisherOnly",)
	clientApplicationTenantIds: Optional[list[str]] = Field(default=None,alias="clientApplicationTenantIds",)
	permissionClassification: Optional[str] = Field(default=None,alias="permissionClassification",)
	permissions: Optional[list[str]] = Field(default=None,alias="permissions",)
	permissionType: Optional[PermissionType] = Field(default=None,alias="permissionType",)
	resourceApplication: Optional[str] = Field(default=None,alias="resourceApplication",)

from .permission_type import PermissionType

