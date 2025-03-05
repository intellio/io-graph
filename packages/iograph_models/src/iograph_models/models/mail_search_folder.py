from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailSearchFolder(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	childFolderCount: Optional[int] = Field(default=None,alias="childFolderCount",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isHidden: Optional[bool] = Field(default=None,alias="isHidden",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	totalItemCount: Optional[int] = Field(default=None,alias="totalItemCount",)
	unreadItemCount: Optional[int] = Field(default=None,alias="unreadItemCount",)
	childFolders: Optional[list[MailFolder]] = Field(default=None,alias="childFolders",)
	messageRules: Optional[list[MessageRule]] = Field(default=None,alias="messageRules",)
	messages: Optional[list[Message]] = Field(default=None,alias="messages",)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(default=None,alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="singleValueExtendedProperties",)
	filterQuery: Optional[str] = Field(default=None,alias="filterQuery",)
	includeNestedFolders: Optional[bool] = Field(default=None,alias="includeNestedFolders",)
	isSupported: Optional[bool] = Field(default=None,alias="isSupported",)
	sourceFolderIds: Optional[list[str]] = Field(default=None,alias="sourceFolderIds",)

from .mail_folder import MailFolder
from .message_rule import MessageRule
from .message import Message
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

