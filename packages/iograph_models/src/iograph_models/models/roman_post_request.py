from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RomanPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	form: Optional[str] = Field(default=None,alias="form",)


