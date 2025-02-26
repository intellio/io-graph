from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Website(BaseModel):
	address: Optional[str] = Field(default=None,alias="address",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	type: Optional[WebsiteType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .website_type import WebsiteType

