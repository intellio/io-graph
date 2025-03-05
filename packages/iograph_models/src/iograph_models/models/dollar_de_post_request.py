from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Dollar_dePostRequest(BaseModel):
	fractionalDollar: Optional[str] = Field(default=None,alias="fractionalDollar",)
	fraction: Optional[str] = Field(default=None,alias="fraction",)


