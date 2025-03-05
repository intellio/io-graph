from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailSearchFolder(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	childFolderCount: Optional[int] = Field(alias="childFolderCount",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isHidden: Optional[bool] = Field(alias="isHidden",default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId",default=None,)
	totalItemCount: Optional[int] = Field(alias="totalItemCount",default=None,)
	unreadItemCount: Optional[int] = Field(alias="unreadItemCount",default=None,)
	childFolders: SerializeAsAny[Optional[list[MailFolder]]] = Field(alias="childFolders",default=None,)
	messageRules: Optional[list[MessageRule]] = Field(alias="messageRules",default=None,)
	messages: SerializeAsAny[Optional[list[Message]]] = Field(alias="messages",default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties",default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties",default=None,)
	filterQuery: Optional[str] = Field(alias="filterQuery",default=None,)
	includeNestedFolders: Optional[bool] = Field(alias="includeNestedFolders",default=None,)
	isSupported: Optional[bool] = Field(alias="isSupported",default=None,)
	sourceFolderIds: Optional[list[str]] = Field(alias="sourceFolderIds",default=None,)

from .mail_folder import MailFolder
from .message_rule import MessageRule
from .message import Message
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

