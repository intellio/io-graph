from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceEnrollmentLimitConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceEnrollmentLimitConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.deviceEnrollmentLimitConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="assignments", default=None,)
	limit: Optional[int] = Field(alias="limit", default=None,)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
