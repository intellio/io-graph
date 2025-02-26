from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmailAddress(BaseModel):
	address: Optional[str] = Field(default=None,alias="address",)
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


