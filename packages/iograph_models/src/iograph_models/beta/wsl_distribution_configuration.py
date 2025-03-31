from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WslDistributionConfiguration(BaseModel):
	distribution: Optional[str] = Field(alias="distribution", default=None,)
	maximumOSVersion: Optional[str] = Field(alias="maximumOSVersion", default=None,)
	minimumOSVersion: Optional[str] = Field(alias="minimumOSVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

