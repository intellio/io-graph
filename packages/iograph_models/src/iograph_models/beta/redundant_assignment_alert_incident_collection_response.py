from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RedundantAssignmentAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[RedundantAssignmentAlertIncident]] = Field(alias="value", default=None,)

from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident

