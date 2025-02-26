from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintSettings(BaseModel):
	documentConversionEnabled: Optional[bool] = Field(default=None,alias="documentConversionEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


