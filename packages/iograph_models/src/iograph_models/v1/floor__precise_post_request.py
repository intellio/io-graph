from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Floor__precisePostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	significance: Optional[str] = Field(alias="significance", default=None,)


