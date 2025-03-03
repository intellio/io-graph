from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SamlSingleSignOnSettings(BaseModel):
	relayState: Optional[str] = Field(default=None,alias="relayState",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


