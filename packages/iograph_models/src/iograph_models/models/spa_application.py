from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SpaApplication(BaseModel):
	redirectUris: list[str] = Field(alias="redirectUris",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


