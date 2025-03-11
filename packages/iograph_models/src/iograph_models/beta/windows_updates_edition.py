from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesEdition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceFamily: Optional[str] = Field(alias="deviceFamily",default=None,)
	endOfServiceDateTime: Optional[datetime] = Field(alias="endOfServiceDateTime",default=None,)
	generalAvailabilityDateTime: Optional[datetime] = Field(alias="generalAvailabilityDateTime",default=None,)
	isInService: Optional[bool] = Field(alias="isInService",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	releasedName: Optional[str] = Field(alias="releasedName",default=None,)
	servicingPeriods: Optional[list[WindowsUpdatesServicingPeriod]] = Field(alias="servicingPeriods",default=None,)

from .windows_updates_servicing_period import WindowsUpdatesServicingPeriod

