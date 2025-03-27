from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxFolder(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	childFolderCount: Optional[int] = Field(alias="childFolderCount", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	parentMailboxUrl: Optional[str] = Field(alias="parentMailboxUrl", default=None,)
	totalItemCount: Optional[int] = Field(alias="totalItemCount", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	childFolders: Optional[list[MailboxFolder]] = Field(alias="childFolders", default=None,)
	items: Optional[list[MailboxItem]] = Field(alias="items", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .mailbox_item import MailboxItem
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

