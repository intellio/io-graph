from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class InvitedUserMessageInfo(BaseModel):
	ccRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="ccRecipients", default=None,)
	customizedMessageBody: Optional[str] = Field(alias="customizedMessageBody", default=None,)
	messageLanguage: Optional[str] = Field(alias="messageLanguage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .attendee_base import AttendeeBase
from .attendee import Attendee

