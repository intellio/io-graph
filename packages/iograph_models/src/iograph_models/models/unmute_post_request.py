from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnmutePostRequest(BaseModel):
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)


