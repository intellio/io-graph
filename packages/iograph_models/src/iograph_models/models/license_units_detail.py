from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LicenseUnitsDetail(BaseModel):
	enabled: Optional[int] = Field(default=None,alias="enabled",)
	lockedOut: Optional[int] = Field(default=None,alias="lockedOut",)
	suspended: Optional[int] = Field(default=None,alias="suspended",)
	warning: Optional[int] = Field(default=None,alias="warning",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


