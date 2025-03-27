from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySmsDeletePhoneNumberRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.smsDeletePhoneNumberRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.smsDeletePhoneNumberRecord")


