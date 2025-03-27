from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Trim_meanPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)
	percent: Optional[str] = Field(alias="percent", default=None,)


