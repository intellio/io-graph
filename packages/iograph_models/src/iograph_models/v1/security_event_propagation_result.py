from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEventPropagationResult(BaseModel):
	location: Optional[str] = Field(alias="location", default=None,)
	serviceName: Optional[str] = Field(alias="serviceName", default=None,)
	status: Optional[SecurityEventPropagationStatus | str] = Field(alias="status", default=None,)
	statusInformation: Optional[str] = Field(alias="statusInformation", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_event_propagation_status import SecurityEventPropagationStatus

