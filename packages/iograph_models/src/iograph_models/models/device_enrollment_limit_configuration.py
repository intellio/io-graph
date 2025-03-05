from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceEnrollmentLimitConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(default=None,alias="assignments",)
	limit: Optional[int] = Field(default=None,alias="limit",)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment

