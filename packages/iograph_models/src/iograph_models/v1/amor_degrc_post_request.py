from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Amor_degrcPostRequest(BaseModel):
	cost: Optional[str] = Field(alias="cost", default=None,)
	datePurchased: Optional[str] = Field(alias="datePurchased", default=None,)
	firstPeriod: Optional[str] = Field(alias="firstPeriod", default=None,)
	salvage: Optional[str] = Field(alias="salvage", default=None,)
	period: Optional[str] = Field(alias="period", default=None,)
	rate: Optional[str] = Field(alias="rate", default=None,)
	basis: Optional[str] = Field(alias="basis", default=None,)

