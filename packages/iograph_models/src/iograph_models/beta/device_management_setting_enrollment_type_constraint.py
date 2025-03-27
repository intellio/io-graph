from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingEnrollmentTypeConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint")
	enrollmentTypes: Optional[list[str]] = Field(alias="enrollmentTypes", default=None,)


