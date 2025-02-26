from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmailSettings(BaseModel):
	senderDomain: Optional[str] = Field(default=None,alias="senderDomain",)
	useCompanyBranding: Optional[bool] = Field(default=None,alias="useCompanyBranding",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


