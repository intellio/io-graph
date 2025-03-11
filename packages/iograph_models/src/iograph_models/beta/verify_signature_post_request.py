from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Verify_signaturePostRequest(BaseModel):
	digest: Optional[str] = Field(alias="digest",default=None,)
	signature: Optional[str] = Field(alias="signature",default=None,)
	signingKeyId: Optional[str] = Field(alias="signingKeyId",default=None,)


