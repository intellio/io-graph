from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VerificationResult(BaseModel):
	signatureValid: Optional[bool] = Field(alias="signatureValid", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

