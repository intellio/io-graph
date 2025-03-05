from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionGrantConditionSet(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	clientApplicationIds: Optional[list[str]] = Field(alias="clientApplicationIds",default=None,)
	clientApplicationPublisherIds: Optional[list[str]] = Field(alias="clientApplicationPublisherIds",default=None,)
	clientApplicationsFromVerifiedPublisherOnly: Optional[bool] = Field(alias="clientApplicationsFromVerifiedPublisherOnly",default=None,)
	clientApplicationTenantIds: Optional[list[str]] = Field(alias="clientApplicationTenantIds",default=None,)
	permissionClassification: Optional[str] = Field(alias="permissionClassification",default=None,)
	permissions: Optional[list[str]] = Field(alias="permissions",default=None,)
	permissionType: Optional[PermissionType | str] = Field(alias="permissionType",default=None,)
	resourceApplication: Optional[str] = Field(alias="resourceApplication",default=None,)

from .permission_type import PermissionType

