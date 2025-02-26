from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MessageRulePredicates(BaseModel):
	bodyContains: list[Optional[str]] = Field(alias="bodyContains",)
	bodyOrSubjectContains: list[Optional[str]] = Field(alias="bodyOrSubjectContains",)
	categories: list[Optional[str]] = Field(alias="categories",)
	fromAddresses: list[Recipient] = Field(alias="fromAddresses",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	headerContains: list[Optional[str]] = Field(alias="headerContains",)
	importance: Optional[Importance] = Field(default=None,alias="importance",)
	isApprovalRequest: Optional[bool] = Field(default=None,alias="isApprovalRequest",)
	isAutomaticForward: Optional[bool] = Field(default=None,alias="isAutomaticForward",)
	isAutomaticReply: Optional[bool] = Field(default=None,alias="isAutomaticReply",)
	isEncrypted: Optional[bool] = Field(default=None,alias="isEncrypted",)
	isMeetingRequest: Optional[bool] = Field(default=None,alias="isMeetingRequest",)
	isMeetingResponse: Optional[bool] = Field(default=None,alias="isMeetingResponse",)
	isNonDeliveryReport: Optional[bool] = Field(default=None,alias="isNonDeliveryReport",)
	isPermissionControlled: Optional[bool] = Field(default=None,alias="isPermissionControlled",)
	isReadReceipt: Optional[bool] = Field(default=None,alias="isReadReceipt",)
	isSigned: Optional[bool] = Field(default=None,alias="isSigned",)
	isVoicemail: Optional[bool] = Field(default=None,alias="isVoicemail",)
	messageActionFlag: Optional[MessageActionFlag] = Field(default=None,alias="messageActionFlag",)
	notSentToMe: Optional[bool] = Field(default=None,alias="notSentToMe",)
	recipientContains: list[Optional[str]] = Field(alias="recipientContains",)
	senderContains: list[Optional[str]] = Field(alias="senderContains",)
	sensitivity: Optional[Sensitivity] = Field(default=None,alias="sensitivity",)
	sentCcMe: Optional[bool] = Field(default=None,alias="sentCcMe",)
	sentOnlyToMe: Optional[bool] = Field(default=None,alias="sentOnlyToMe",)
	sentToAddresses: list[Recipient] = Field(alias="sentToAddresses",)
	sentToMe: Optional[bool] = Field(default=None,alias="sentToMe",)
	sentToOrCcMe: Optional[bool] = Field(default=None,alias="sentToOrCcMe",)
	subjectContains: list[Optional[str]] = Field(alias="subjectContains",)
	withinSizeRange: Optional[SizeRange] = Field(default=None,alias="withinSizeRange",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recipient import Recipient
from .importance import Importance
from .message_action_flag import MessageActionFlag
from .sensitivity import Sensitivity
from .recipient import Recipient
from .size_range import SizeRange

