from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CollapseProperty(BaseModel):
	fields: list[str] = Field(alias="fields",)
	limit: Optional[int] = Field(default=None,alias="limit",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


