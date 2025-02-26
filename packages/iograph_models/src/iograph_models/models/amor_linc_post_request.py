from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Amor_lincPostRequest(BaseModel):
	cost: Optional[str] = Field(default=None,alias="cost",)
	datePurchased: Optional[str] = Field(default=None,alias="datePurchased",)
	firstPeriod: Optional[str] = Field(default=None,alias="firstPeriod",)
	salvage: Optional[str] = Field(default=None,alias="salvage",)
	period: Optional[str] = Field(default=None,alias="period",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	basis: Optional[str] = Field(default=None,alias="basis",)


