from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySmsCreatePhoneNumberRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.smsCreatePhoneNumberRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.smsCreatePhoneNumberRecord")

