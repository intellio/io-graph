from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeleteAction(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	objectType: Optional[str] = Field(default=None,alias="objectType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


