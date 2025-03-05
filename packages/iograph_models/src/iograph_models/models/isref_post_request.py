from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IsrefPostRequest(BaseModel):
	value: Optional[str] = Field(default=None,alias="value",)


