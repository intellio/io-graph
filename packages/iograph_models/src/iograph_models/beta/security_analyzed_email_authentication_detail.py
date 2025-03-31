from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAnalyzedEmailAuthenticationDetail(BaseModel):
	compositeAuthentication: Optional[str] = Field(alias="compositeAuthentication", default=None,)
	dkim: Optional[str] = Field(alias="dkim", default=None,)
	dmarc: Optional[str] = Field(alias="dmarc", default=None,)
	senderPolicyFramework: Optional[str] = Field(alias="senderPolicyFramework", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

