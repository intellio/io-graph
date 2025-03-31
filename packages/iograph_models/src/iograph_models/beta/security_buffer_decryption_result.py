from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityBufferDecryptionResult(BaseModel):
	decryptedBuffer: Optional[str] = Field(alias="decryptedBuffer", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

