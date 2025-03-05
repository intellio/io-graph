from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ValuePostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)


