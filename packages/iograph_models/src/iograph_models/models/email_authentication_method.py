from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmailAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)


