from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Generate_encryption_public_keyPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)


