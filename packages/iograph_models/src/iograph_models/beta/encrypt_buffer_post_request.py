from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Encrypt_bufferPostRequest(BaseModel):
	buffer: Optional[str] = Field(alias="buffer", default=None,)
	labelId: Optional[UUID] = Field(alias="labelId", default=None,)


