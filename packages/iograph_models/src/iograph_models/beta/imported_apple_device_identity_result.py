from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ImportedAppleDeviceIdentityResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	discoverySource: Optional[DiscoverySource | str] = Field(alias="discoverySource", default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted", default=None,)
	isSupervised: Optional[bool] = Field(alias="isSupervised", default=None,)
	lastContactedDateTime: Optional[datetime] = Field(alias="lastContactedDateTime", default=None,)
	platform: Optional[Platform | str] = Field(alias="platform", default=None,)
	requestedEnrollmentProfileAssignmentDateTime: Optional[datetime] = Field(alias="requestedEnrollmentProfileAssignmentDateTime", default=None,)
	requestedEnrollmentProfileId: Optional[str] = Field(alias="requestedEnrollmentProfileId", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	status: Optional[bool] = Field(alias="status", default=None,)

from .discovery_source import DiscoverySource
from .enrollment_state import EnrollmentState
from .platform import Platform

