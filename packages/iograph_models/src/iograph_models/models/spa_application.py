from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SpaApplication(BaseModel):
	redirectUris: Optional[list[str]] = Field(default=None,alias="redirectUris",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


