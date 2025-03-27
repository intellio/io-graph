from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SequentialActivationRenewalsAlertIncidentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SequentialActivationRenewalsAlertIncident]] = Field(alias="value", default=None,)

from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident

