from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MailTips(BaseModel):
	automaticReplies: Optional[AutomaticRepliesMailTips] = Field(default=None,alias="automaticReplies",)
	customMailTip: Optional[str] = Field(default=None,alias="customMailTip",)
	deliveryRestricted: Optional[bool] = Field(default=None,alias="deliveryRestricted",)
	emailAddress: Optional[EmailAddress] = Field(default=None,alias="emailAddress",)
	error: Optional[MailTipsError] = Field(default=None,alias="error",)
	externalMemberCount: Optional[int] = Field(default=None,alias="externalMemberCount",)
	isModerated: Optional[bool] = Field(default=None,alias="isModerated",)
	mailboxFull: Optional[bool] = Field(default=None,alias="mailboxFull",)
	maxMessageSize: Optional[int] = Field(default=None,alias="maxMessageSize",)
	recipientScope: Optional[RecipientScopeType] = Field(default=None,alias="recipientScope",)
	recipientSuggestions: list[Recipient] = Field(alias="recipientSuggestions",)
	totalMemberCount: Optional[int] = Field(default=None,alias="totalMemberCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .automatic_replies_mail_tips import AutomaticRepliesMailTips
from .email_address import EmailAddress
from .mail_tips_error import MailTipsError
from .recipient_scope_type import RecipientScopeType
from .recipient import Recipient

