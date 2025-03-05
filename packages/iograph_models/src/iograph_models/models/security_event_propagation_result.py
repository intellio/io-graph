from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEventPropagationResult(BaseModel):
	location: Optional[str] = Field(default=None,alias="location",)
	serviceName: Optional[str] = Field(default=None,alias="serviceName",)
	status: Optional[SecurityEventPropagationStatus] = Field(default=None,alias="status",)
	statusInformation: Optional[str] = Field(default=None,alias="statusInformation",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_event_propagation_status import SecurityEventPropagationStatus

