from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySensorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecuritySensor]] = Field(alias="value", default=None,)

from .security_sensor import SecuritySensor
