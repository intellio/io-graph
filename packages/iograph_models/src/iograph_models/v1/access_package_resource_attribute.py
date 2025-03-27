from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceAttribute(BaseModel):
	destination: Optional[Union[AccessPackageUserDirectoryAttributeStore]] = Field(alias="destination", default=None,discriminator="odata_type", )
	isEditable: Optional[bool] = Field(alias="isEditable", default=None,)
	isPersistedOnAssignmentRemoval: Optional[bool] = Field(alias="isPersistedOnAssignmentRemoval", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	source: Optional[Union[AccessPackageResourceAttributeQuestion]] = Field(alias="source", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_package_user_directory_attribute_store import AccessPackageUserDirectoryAttributeStore
from .access_package_resource_attribute_question import AccessPackageResourceAttributeQuestion

