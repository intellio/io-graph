from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySigningResult(BaseModel):
	signature: Optional[str] = Field(alias="signature", default=None,)
	signingKeyId: Optional[str] = Field(alias="signingKeyId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

