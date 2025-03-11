from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UploadPostRequest(BaseModel):
	uploadUrl: Optional[str] = Field(alias="uploadUrl",default=None,)
	sha256FileHash: Optional[str] = Field(alias="sha256FileHash",default=None,)


