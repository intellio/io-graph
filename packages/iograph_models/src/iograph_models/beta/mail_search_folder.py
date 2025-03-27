from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MailSearchFolder(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mailSearchFolder"] = Field(alias="@odata.type", default="#microsoft.graph.mailSearchFolder")
	childFolderCount: Optional[int] = Field(alias="childFolderCount", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isHidden: Optional[bool] = Field(alias="isHidden", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	totalItemCount: Optional[int] = Field(alias="totalItemCount", default=None,)
	unreadItemCount: Optional[int] = Field(alias="unreadItemCount", default=None,)
	wellKnownName: Optional[str] = Field(alias="wellKnownName", default=None,)
	childFolders: Optional[list[Annotated[Union[MailSearchFolder],Field(discriminator="odata_type")]]] = Field(alias="childFolders", default=None,)
	messageRules: Optional[list[MessageRule]] = Field(alias="messageRules", default=None,)
	messages: Optional[list[Annotated[Union[CalendarSharingMessage, EventMessage, EventMessageRequest, EventMessageResponse],Field(discriminator="odata_type")]]] = Field(alias="messages", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	operations: Optional[list[Annotated[Union[UpdateAllMessagesReadStateOperation],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)
	userConfigurations: Optional[list[UserConfiguration]] = Field(alias="userConfigurations", default=None,)
	filterQuery: Optional[str] = Field(alias="filterQuery", default=None,)
	includeNestedFolders: Optional[bool] = Field(alias="includeNestedFolders", default=None,)
	isSupported: Optional[bool] = Field(alias="isSupported", default=None,)
	sourceFolderIds: Optional[list[str]] = Field(alias="sourceFolderIds", default=None,)

from .message_rule import MessageRule
from .calendar_sharing_message import CalendarSharingMessage
from .event_message import EventMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from .user_configuration import UserConfiguration

