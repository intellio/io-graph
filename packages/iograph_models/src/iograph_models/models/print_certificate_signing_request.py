from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintCertificateSigningRequest(BaseModel):
	content: Optional[str] = Field(default=None,alias="content",)
	transportKey: Optional[str] = Field(default=None,alias="transportKey",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


