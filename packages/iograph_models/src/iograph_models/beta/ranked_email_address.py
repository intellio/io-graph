from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RankedEmailAddress(BaseModel):
	address: Optional[str] = Field(alias="address",default=None,)
	rank: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric

