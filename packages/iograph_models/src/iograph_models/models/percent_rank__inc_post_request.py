from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Percent_rank__incPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array",default=None,)
	x: Optional[str] = Field(alias="x",default=None,)
	significance: Optional[str] = Field(alias="significance",default=None,)


