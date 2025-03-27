from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVendorInformation(BaseModel):
	provider: Optional[str] = Field(alias="provider", default=None,)
	providerVersion: Optional[str] = Field(alias="providerVersion", default=None,)
	subProvider: Optional[str] = Field(alias="subProvider", default=None,)
	vendor: Optional[str] = Field(alias="vendor", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


