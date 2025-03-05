from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceAttribute(BaseModel):
	destination: SerializeAsAny[Optional[AccessPackageResourceAttributeDestination]] = Field(default=None,alias="destination",)
	isEditable: Optional[bool] = Field(default=None,alias="isEditable",)
	isPersistedOnAssignmentRemoval: Optional[bool] = Field(default=None,alias="isPersistedOnAssignmentRemoval",)
	name: Optional[str] = Field(default=None,alias="name",)
	source: SerializeAsAny[Optional[AccessPackageResourceAttributeSource]] = Field(default=None,alias="source",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

