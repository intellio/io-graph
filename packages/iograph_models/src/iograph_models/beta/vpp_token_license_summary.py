from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VppTokenLicenseSummary(BaseModel):
	appleId: Optional[str] = Field(alias="appleId", default=None,)
	availableLicenseCount: Optional[int] = Field(alias="availableLicenseCount", default=None,)
	organizationName: Optional[str] = Field(alias="organizationName", default=None,)
	usedLicenseCount: Optional[int] = Field(alias="usedLicenseCount", default=None,)
	vppTokenId: Optional[str] = Field(alias="vppTokenId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


