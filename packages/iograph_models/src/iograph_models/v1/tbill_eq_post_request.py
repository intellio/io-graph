from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Tbill_eqPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement",default=None,)
	maturity: Optional[str] = Field(alias="maturity",default=None,)
	discount: Optional[str] = Field(alias="discount",default=None,)


