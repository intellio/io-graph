from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ContactFolder(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	childFolders: list[ContactFolder] = Field(alias="childFolders",)
	contacts: list[Contact] = Field(alias="contacts",)
	multiValueExtendedProperties: list[MultiValueLegacyExtendedProperty] = Field(alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: list[SingleValueLegacyExtendedProperty] = Field(alias="singleValueExtendedProperties",)

from .contact import Contact
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

