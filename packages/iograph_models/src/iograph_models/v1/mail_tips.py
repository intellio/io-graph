from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MailTips(BaseModel):
	automaticReplies: Optional[AutomaticRepliesMailTips] = Field(alias="automaticReplies", default=None,)
	customMailTip: Optional[str] = Field(alias="customMailTip", default=None,)
	deliveryRestricted: Optional[bool] = Field(alias="deliveryRestricted", default=None,)
	emailAddress: Optional[EmailAddress] = Field(alias="emailAddress", default=None,)
	error: Optional[MailTipsError] = Field(alias="error", default=None,)
	externalMemberCount: Optional[int] = Field(alias="externalMemberCount", default=None,)
	isModerated: Optional[bool] = Field(alias="isModerated", default=None,)
	mailboxFull: Optional[bool] = Field(alias="mailboxFull", default=None,)
	maxMessageSize: Optional[int] = Field(alias="maxMessageSize", default=None,)
	recipientScope: Optional[RecipientScopeType | str] = Field(alias="recipientScope", default=None,)
	recipientSuggestions: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="recipientSuggestions", default=None,)
	totalMemberCount: Optional[int] = Field(alias="totalMemberCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .automatic_replies_mail_tips import AutomaticRepliesMailTips
from .email_address import EmailAddress
from .mail_tips_error import MailTipsError
from .recipient_scope_type import RecipientScopeType
from .attendee_base import AttendeeBase
from .attendee import Attendee

