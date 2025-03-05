from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attachments: Optional[list[ChatMessageAttachment]] = Field(alias="attachments",default=None,)
	body: Optional[ItemBody] = Field(alias="body",default=None,)
	channelIdentity: Optional[ChannelIdentity] = Field(alias="channelIdentity",default=None,)
	chatId: Optional[str] = Field(alias="chatId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	etag: Optional[str] = Field(alias="etag",default=None,)
	eventDetail: SerializeAsAny[Optional[EventMessageDetail]] = Field(alias="eventDetail",default=None,)
	from_: Optional[ChatMessageFromIdentitySet] = Field(alias="from",default=None,)
	importance: Optional[str | ChatMessageImportance] = Field(alias="importance",default=None,)
	lastEditedDateTime: Optional[datetime] = Field(alias="lastEditedDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	locale: Optional[str] = Field(alias="locale",default=None,)
	mentions: Optional[list[ChatMessageMention]] = Field(alias="mentions",default=None,)
	messageHistory: Optional[list[ChatMessageHistoryItem]] = Field(alias="messageHistory",default=None,)
	messageType: Optional[str | ChatMessageType] = Field(alias="messageType",default=None,)
	policyViolation: Optional[ChatMessagePolicyViolation] = Field(alias="policyViolation",default=None,)
	reactions: Optional[list[ChatMessageReaction]] = Field(alias="reactions",default=None,)
	replyToId: Optional[str] = Field(alias="replyToId",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	summary: Optional[str] = Field(alias="summary",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	hostedContents: Optional[list[ChatMessageHostedContent]] = Field(alias="hostedContents",default=None,)
	replies: Optional[list[ChatMessage]] = Field(alias="replies",default=None,)

from .chat_message_attachment import ChatMessageAttachment
from .item_body import ItemBody
from .channel_identity import ChannelIdentity
from .event_message_detail import EventMessageDetail
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_importance import ChatMessageImportance
from .chat_message_mention import ChatMessageMention
from .chat_message_history_item import ChatMessageHistoryItem
from .chat_message_type import ChatMessageType
from .chat_message_policy_violation import ChatMessagePolicyViolation
from .chat_message_reaction import ChatMessageReaction
from .chat_message_hosted_content import ChatMessageHostedContent

