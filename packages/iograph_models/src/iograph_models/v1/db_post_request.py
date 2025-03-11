from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DbPostRequest(BaseModel):
	cost: Optional[str] = Field(alias="cost",default=None,)
	salvage: Optional[str] = Field(alias="salvage",default=None,)
	life: Optional[str] = Field(alias="life",default=None,)
	period: Optional[str] = Field(alias="period",default=None,)
	month: Optional[str] = Field(alias="month",default=None,)


