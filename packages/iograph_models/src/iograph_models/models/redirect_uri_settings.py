from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RedirectUriSettings(BaseModel):
	index: Optional[int] = Field(default=None,alias="index",)
	uri: Optional[str] = Field(default=None,alias="uri",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


