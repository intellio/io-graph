from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Dollar_frPostRequest(BaseModel):
	decimalDollar: Optional[str] = Field(alias="decimalDollar",default=None,)
	fraction: Optional[str] = Field(alias="fraction",default=None,)


