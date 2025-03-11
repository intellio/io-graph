from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceAttribute(BaseModel):
	attributeDestination: SerializeAsAny[Optional[AccessPackageResourceAttributeDestination]] = Field(alias="attributeDestination",default=None,)
	attributeName: Optional[str] = Field(alias="attributeName",default=None,)
	attributeSource: SerializeAsAny[Optional[AccessPackageResourceAttributeSource]] = Field(alias="attributeSource",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	isEditable: Optional[bool] = Field(alias="isEditable",default=None,)
	isPersistedOnAssignmentRemoval: Optional[bool] = Field(alias="isPersistedOnAssignmentRemoval",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

