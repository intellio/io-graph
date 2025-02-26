from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PermissionGrantConditionSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientApplicationIds: list[Optional[str]] = Field(alias="clientApplicationIds",)
	clientApplicationPublisherIds: list[Optional[str]] = Field(alias="clientApplicationPublisherIds",)
	clientApplicationsFromVerifiedPublisherOnly: Optional[bool] = Field(default=None,alias="clientApplicationsFromVerifiedPublisherOnly",)
	clientApplicationTenantIds: list[Optional[str]] = Field(alias="clientApplicationTenantIds",)
	permissionClassification: Optional[str] = Field(default=None,alias="permissionClassification",)
	permissions: list[Optional[str]] = Field(alias="permissions",)
	permissionType: Optional[PermissionType] = Field(default=None,alias="permissionType",)
	resourceApplication: Optional[str] = Field(default=None,alias="resourceApplication",)

from .permission_type import PermissionType

