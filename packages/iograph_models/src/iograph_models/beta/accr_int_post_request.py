from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Accr_intPostRequest(BaseModel):
	issue: Optional[str] = Field(alias="issue",default=None,)
	firstInterest: Optional[str] = Field(alias="firstInterest",default=None,)
	settlement: Optional[str] = Field(alias="settlement",default=None,)
	rate: Optional[str] = Field(alias="rate",default=None,)
	par: Optional[str] = Field(alias="par",default=None,)
	frequency: Optional[str] = Field(alias="frequency",default=None,)
	basis: Optional[str] = Field(alias="basis",default=None,)
	calcMethod: Optional[str] = Field(alias="calcMethod",default=None,)


