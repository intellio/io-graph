from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Album(BaseModel):
	coverImageItemId: Optional[str] = Field(alias="coverImageItemId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

