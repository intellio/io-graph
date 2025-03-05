from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DollarPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number",default=None,)
	decimals: Optional[str] = Field(alias="decimals",default=None,)


