from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityEdiscoveryCaseMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoveryCaseMember"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoveryCaseMember")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	recipientType: Optional[SecurityRecipientType | str] = Field(alias="recipientType", default=None,)
	smtpAddress: Optional[str] = Field(alias="smtpAddress", default=None,)

from .security_recipient_type import SecurityRecipientType
