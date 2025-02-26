from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OptionalClaim(BaseModel):
	additionalProperties: list[Optional[str]] = Field(alias="additionalProperties",)
	essential: Optional[bool] = Field(default=None,alias="essential",)
	name: Optional[str] = Field(default=None,alias="name",)
	source: Optional[str] = Field(default=None,alias="source",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


