from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnEmailOtpSendListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OnEmailOtpSendListener]] = Field(alias="value", default=None,)

from .on_email_otp_send_listener import OnEmailOtpSendListener

