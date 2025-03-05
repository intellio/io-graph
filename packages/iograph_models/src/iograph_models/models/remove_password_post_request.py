from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Remove_passwordPostRequest(BaseModel):
	keyId: Optional[UUID] = Field(default=None,alias="keyId",)


