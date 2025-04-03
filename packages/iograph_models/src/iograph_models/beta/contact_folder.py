from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ContactFolder(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.contactFolder"] = Field(alias="@odata.type", default="#microsoft.graph.contactFolder")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	wellKnownName: Optional[str] = Field(alias="wellKnownName", default=None,)
	childFolders: Optional[list[ContactFolder]] = Field(alias="childFolders", default=None,)
	contacts: Optional[list[Contact]] = Field(alias="contacts", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .contact import Contact
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
