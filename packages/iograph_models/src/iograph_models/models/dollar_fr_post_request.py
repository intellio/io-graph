from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Dollar_frPostRequest(BaseModel):
	decimalDollar: Optional[str] = Field(default=None,alias="decimalDollar",)
	fraction: Optional[str] = Field(default=None,alias="fraction",)


