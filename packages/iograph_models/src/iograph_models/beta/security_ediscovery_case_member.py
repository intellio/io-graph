from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCaseMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	recipientType: Optional[SecurityRecipientType | str] = Field(alias="recipientType", default=None,)
	smtpAddress: Optional[str] = Field(alias="smtpAddress", default=None,)

from .security_recipient_type import SecurityRecipientType

