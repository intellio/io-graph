from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DbPostRequest(BaseModel):
	cost: Optional[str] = Field(default=None,alias="cost",)
	salvage: Optional[str] = Field(default=None,alias="salvage",)
	life: Optional[str] = Field(default=None,alias="life",)
	period: Optional[str] = Field(default=None,alias="period",)
	month: Optional[str] = Field(default=None,alias="month",)


