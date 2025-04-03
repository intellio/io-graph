from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class PermissionGrantConditionSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionGrantConditionSet"] = Field(alias="@odata.type", default="#microsoft.graph.permissionGrantConditionSet")
	certifiedClientApplicationsOnly: Optional[bool] = Field(alias="certifiedClientApplicationsOnly", default=None,)
	clientApplicationIds: Optional[list[str]] = Field(alias="clientApplicationIds", default=None,)
	clientApplicationPublisherIds: Optional[list[str]] = Field(alias="clientApplicationPublisherIds", default=None,)
	clientApplicationsFromVerifiedPublisherOnly: Optional[bool] = Field(alias="clientApplicationsFromVerifiedPublisherOnly", default=None,)
	clientApplicationTenantIds: Optional[list[str]] = Field(alias="clientApplicationTenantIds", default=None,)
	permissionClassification: Optional[str] = Field(alias="permissionClassification", default=None,)
	permissions: Optional[list[str]] = Field(alias="permissions", default=None,)
	permissionType: Optional[PermissionType | str] = Field(alias="permissionType", default=None,)
	resourceApplication: Optional[str] = Field(alias="resourceApplication", default=None,)
	scopeSensitivityLabels: Optional[Union[AllScopeSensitivityLabels, EnumeratedScopeSensitivityLabels]] = Field(alias="scopeSensitivityLabels", default=None,discriminator="odata_type", )

from .permission_type import PermissionType
from .all_scope_sensitivity_labels import AllScopeSensitivityLabels
from .enumerated_scope_sensitivity_labels import EnumeratedScopeSensitivityLabels
