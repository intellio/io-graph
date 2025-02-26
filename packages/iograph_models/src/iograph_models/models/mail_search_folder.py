from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailSearchFolder(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	childFolderCount: Optional[int] = Field(default=None,alias="childFolderCount",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isHidden: Optional[bool] = Field(default=None,alias="isHidden",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	totalItemCount: Optional[int] = Field(default=None,alias="totalItemCount",)
	unreadItemCount: Optional[int] = Field(default=None,alias="unreadItemCount",)
	childFolders: list[MailFolder] = Field(alias="childFolders",)
	messageRules: list[MessageRule] = Field(alias="messageRules",)
	messages: list[Message] = Field(alias="messages",)
	multiValueExtendedProperties: list[MultiValueLegacyExtendedProperty] = Field(alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: list[SingleValueLegacyExtendedProperty] = Field(alias="singleValueExtendedProperties",)
	filterQuery: Optional[str] = Field(default=None,alias="filterQuery",)
	includeNestedFolders: Optional[bool] = Field(default=None,alias="includeNestedFolders",)
	isSupported: Optional[bool] = Field(default=None,alias="isSupported",)
	sourceFolderIds: list[Optional[str]] = Field(alias="sourceFolderIds",)

from .mail_folder import MailFolder
from .message_rule import MessageRule
from .message import Message
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

