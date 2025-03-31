from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Decrypt_bufferPostRequest(BaseModel):
	encryptedBuffer: Optional[str] = Field(alias="encryptedBuffer", default=None,)
	publishingLicense: Optional[str] = Field(alias="publishingLicense", default=None,)

