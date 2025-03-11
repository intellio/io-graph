from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class App_diagnostics_with_upnGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PowerliftIncidentMetadata]] = Field(alias="value",default=None,)

from .powerlift_incident_metadata import PowerliftIncidentMetadata

