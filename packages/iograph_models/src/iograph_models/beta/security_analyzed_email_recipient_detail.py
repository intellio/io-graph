from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAnalyzedEmailRecipientDetail(BaseModel):
	ccRecipients: Optional[list[str]] = Field(alias="ccRecipients", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

