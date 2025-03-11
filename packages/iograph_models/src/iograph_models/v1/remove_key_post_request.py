from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Remove_keyPostRequest(BaseModel):
	keyId: Optional[UUID] = Field(alias="keyId",default=None,)
	proof: Optional[str] = Field(alias="proof",default=None,)


