from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityVendorInformation(BaseModel):
	provider: Optional[str] = Field(default=None,alias="provider",)
	providerVersion: Optional[str] = Field(default=None,alias="providerVersion",)
	subProvider: Optional[str] = Field(default=None,alias="subProvider",)
	vendor: Optional[str] = Field(default=None,alias="vendor",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


