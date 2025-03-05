from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceAttribute(BaseModel):
	destination: SerializeAsAny[Optional[AccessPackageResourceAttributeDestination]] = Field(alias="destination",default=None,)
	isEditable: Optional[bool] = Field(alias="isEditable",default=None,)
	isPersistedOnAssignmentRemoval: Optional[bool] = Field(alias="isPersistedOnAssignmentRemoval",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	source: SerializeAsAny[Optional[AccessPackageResourceAttributeSource]] = Field(alias="source",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

