from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AccessPackageResourceAttribute(BaseModel):
	attributeDestination: Optional[Union[AccessPackageUserDirectoryAttributeStore]] = Field(alias="attributeDestination", default=None,discriminator="odata_type", )
	attributeName: Optional[str] = Field(alias="attributeName", default=None,)
	attributeSource: Optional[Union[AccessPackageResourceAttributeQuestion]] = Field(alias="attributeSource", default=None,discriminator="odata_type", )
	id: Optional[str] = Field(alias="id", default=None,)
	isEditable: Optional[bool] = Field(alias="isEditable", default=None,)
	isPersistedOnAssignmentRemoval: Optional[bool] = Field(alias="isPersistedOnAssignmentRemoval", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_package_user_directory_attribute_store import AccessPackageUserDirectoryAttributeStore
from .access_package_resource_attribute_question import AccessPackageResourceAttributeQuestion
