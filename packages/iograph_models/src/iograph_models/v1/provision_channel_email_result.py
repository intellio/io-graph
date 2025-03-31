from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProvisionChannelEmailResult(BaseModel):
	email: Optional[str] = Field(alias="email", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

