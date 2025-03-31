from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEmailSender(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

