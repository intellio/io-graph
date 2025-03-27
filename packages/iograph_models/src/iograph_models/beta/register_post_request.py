from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RegisterPostRequest(BaseModel):
	externalId: Optional[str] = Field(alias="externalId", default=None,)


