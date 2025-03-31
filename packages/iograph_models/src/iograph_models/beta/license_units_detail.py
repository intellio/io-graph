from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LicenseUnitsDetail(BaseModel):
	enabled: Optional[int] = Field(alias="enabled", default=None,)
	lockedOut: Optional[int] = Field(alias="lockedOut", default=None,)
	suspended: Optional[int] = Field(alias="suspended", default=None,)
	warning: Optional[int] = Field(alias="warning", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

