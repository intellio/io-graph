from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReceivedPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement",default=None,)
	maturity: Optional[str] = Field(alias="maturity",default=None,)
	investment: Optional[str] = Field(alias="investment",default=None,)
	discount: Optional[str] = Field(alias="discount",default=None,)
	basis: Optional[str] = Field(alias="basis",default=None,)


