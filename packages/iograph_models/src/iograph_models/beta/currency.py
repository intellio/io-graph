from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Currency(BaseModel):
	amountDecimalPlaces: Optional[str] = Field(alias="amountDecimalPlaces", default=None,)
	amountRoundingPrecision: Optional[int] = Field(alias="amountRoundingPrecision", default=None,)
	code: Optional[str] = Field(alias="code", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	symbol: Optional[str] = Field(alias="symbol", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


