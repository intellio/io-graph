from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHyperlink(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	url: Optional[str] = Field(default=None,alias="url",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


