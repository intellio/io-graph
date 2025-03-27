from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Financials(BaseModel):
	id: Optional[UUID] = Field(alias="id", default=None,)
	companies: Optional[list[Company]] = Field(alias="companies", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .company import Company

