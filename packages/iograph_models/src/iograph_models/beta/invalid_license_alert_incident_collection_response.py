from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvalidLicenseAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[InvalidLicenseAlertIncident]] = Field(alias="value", default=None,)

from .invalid_license_alert_incident import InvalidLicenseAlertIncident

