from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContactFolder(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	childFolders: Optional[list[ContactFolder]] = Field(default=None,alias="childFolders",)
	contacts: Optional[list[Contact]] = Field(default=None,alias="contacts",)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(default=None,alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="singleValueExtendedProperties",)

from .contact import Contact
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

