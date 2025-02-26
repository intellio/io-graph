from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEmailSender(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


