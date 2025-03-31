from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintCertificateSigningRequest(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	transportKey: Optional[str] = Field(alias="transportKey", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

