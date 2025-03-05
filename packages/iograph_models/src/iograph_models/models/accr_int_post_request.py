from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Accr_intPostRequest(BaseModel):
	issue: Optional[str] = Field(default=None,alias="issue",)
	firstInterest: Optional[str] = Field(default=None,alias="firstInterest",)
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	par: Optional[str] = Field(default=None,alias="par",)
	frequency: Optional[str] = Field(default=None,alias="frequency",)
	basis: Optional[str] = Field(default=None,alias="basis",)
	calcMethod: Optional[str] = Field(default=None,alias="calcMethod",)


