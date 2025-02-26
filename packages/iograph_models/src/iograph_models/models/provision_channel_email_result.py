from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProvisionChannelEmailResult(BaseModel):
	email: Optional[str] = Field(default=None,alias="email",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


