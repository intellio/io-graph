from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attachments: Optional[list[ChatMessageAttachment]] = Field(default=None,alias="attachments",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	channelIdentity: Optional[ChannelIdentity] = Field(default=None,alias="channelIdentity",)
	chatId: Optional[str] = Field(default=None,alias="chatId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	etag: Optional[str] = Field(default=None,alias="etag",)
	eventDetail: Optional[EventMessageDetail] = Field(default=None,alias="eventDetail",)
	from_: Optional[ChatMessageFromIdentitySet] = Field(default=None,alias="from",)
	importance: Optional[ChatMessageImportance] = Field(default=None,alias="importance",)
	lastEditedDateTime: Optional[datetime] = Field(default=None,alias="lastEditedDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	mentions: Optional[list[ChatMessageMention]] = Field(default=None,alias="mentions",)
	messageHistory: Optional[list[ChatMessageHistoryItem]] = Field(default=None,alias="messageHistory",)
	messageType: Optional[ChatMessageType] = Field(default=None,alias="messageType",)
	policyViolation: Optional[ChatMessagePolicyViolation] = Field(default=None,alias="policyViolation",)
	reactions: Optional[list[ChatMessageReaction]] = Field(default=None,alias="reactions",)
	replyToId: Optional[str] = Field(default=None,alias="replyToId",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	summary: Optional[str] = Field(default=None,alias="summary",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	hostedContents: Optional[list[ChatMessageHostedContent]] = Field(default=None,alias="hostedContents",)
	replies: Optional[list[ChatMessage]] = Field(default=None,alias="replies",)

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

