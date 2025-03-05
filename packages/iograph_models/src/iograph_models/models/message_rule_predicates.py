from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MessageRulePredicates(BaseModel):
	bodyContains: Optional[list[str]] = Field(alias="bodyContains",default=None,)
	bodyOrSubjectContains: Optional[list[str]] = Field(alias="bodyOrSubjectContains",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	fromAddresses: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="fromAddresses",default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments",default=None,)
	headerContains: Optional[list[str]] = Field(alias="headerContains",default=None,)
	importance: Optional[str | Importance] = Field(alias="importance",default=None,)
	isApprovalRequest: Optional[bool] = Field(alias="isApprovalRequest",default=None,)
	isAutomaticForward: Optional[bool] = Field(alias="isAutomaticForward",default=None,)
	isAutomaticReply: Optional[bool] = Field(alias="isAutomaticReply",default=None,)
	isEncrypted: Optional[bool] = Field(alias="isEncrypted",default=None,)
	isMeetingRequest: Optional[bool] = Field(alias="isMeetingRequest",default=None,)
	isMeetingResponse: Optional[bool] = Field(alias="isMeetingResponse",default=None,)
	isNonDeliveryReport: Optional[bool] = Field(alias="isNonDeliveryReport",default=None,)
	isPermissionControlled: Optional[bool] = Field(alias="isPermissionControlled",default=None,)
	isReadReceipt: Optional[bool] = Field(alias="isReadReceipt",default=None,)
	isSigned: Optional[bool] = Field(alias="isSigned",default=None,)
	isVoicemail: Optional[bool] = Field(alias="isVoicemail",default=None,)
	messageActionFlag: Optional[str | MessageActionFlag] = Field(alias="messageActionFlag",default=None,)
	notSentToMe: Optional[bool] = Field(alias="notSentToMe",default=None,)
	recipientContains: Optional[list[str]] = Field(alias="recipientContains",default=None,)
	senderContains: Optional[list[str]] = Field(alias="senderContains",default=None,)
	sensitivity: Optional[str | Sensitivity] = Field(alias="sensitivity",default=None,)
	sentCcMe: Optional[bool] = Field(alias="sentCcMe",default=None,)
	sentOnlyToMe: Optional[bool] = Field(alias="sentOnlyToMe",default=None,)
	sentToAddresses: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="sentToAddresses",default=None,)
	sentToMe: Optional[bool] = Field(alias="sentToMe",default=None,)
	sentToOrCcMe: Optional[bool] = Field(alias="sentToOrCcMe",default=None,)
	subjectContains: Optional[list[str]] = Field(alias="subjectContains",default=None,)
	withinSizeRange: Optional[SizeRange] = Field(alias="withinSizeRange",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .recipient import Recipient
from .importance import Importance
from .message_action_flag import MessageActionFlag
from .sensitivity import Sensitivity
from .recipient import Recipient
from .size_range import SizeRange

