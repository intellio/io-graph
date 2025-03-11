from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBufferEncryptionResult(BaseModel):
	encryptedBuffer: Optional[str] = Field(alias="encryptedBuffer",default=None,)
	publishingLicense: Optional[str] = Field(alias="publishingLicense",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


