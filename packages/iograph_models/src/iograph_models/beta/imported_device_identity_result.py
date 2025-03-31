from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ImportedDeviceIdentityResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.importedDeviceIdentityResult"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	importedDeviceIdentifier: Optional[str] = Field(alias="importedDeviceIdentifier", default=None,)
	importedDeviceIdentityType: Optional[ImportedDeviceIdentityType | str] = Field(alias="importedDeviceIdentityType", default=None,)
	lastContactedDateTime: Optional[datetime] = Field(alias="lastContactedDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	platform: Optional[Platform | str] = Field(alias="platform", default=None,)
	status: Optional[bool] = Field(alias="status", default=None,)

from .enrollment_state import EnrollmentState
from .imported_device_identity_type import ImportedDeviceIdentityType
from .platform import Platform
