from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_remove_holdPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(default=None,alias="ids",)


