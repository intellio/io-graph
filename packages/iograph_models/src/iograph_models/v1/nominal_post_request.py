from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NominalPostRequest(BaseModel):
	effectRate: Optional[str] = Field(alias="effectRate", default=None,)
	npery: Optional[str] = Field(alias="npery", default=None,)


