from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CollapseProperty(BaseModel):
	fields: Optional[list[str]] = Field(alias="fields", default=None,)
	limit: Optional[int] = Field(alias="limit", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

