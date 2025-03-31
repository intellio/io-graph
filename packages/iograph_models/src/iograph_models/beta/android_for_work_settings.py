from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidForWorkSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidForWorkSettings"] = Field(alias="@odata.type",)
	bindStatus: Optional[AndroidForWorkBindStatus | str] = Field(alias="bindStatus", default=None,)
	deviceOwnerManagementEnabled: Optional[bool] = Field(alias="deviceOwnerManagementEnabled", default=None,)
	enrollmentTarget: Optional[AndroidForWorkEnrollmentTarget | str] = Field(alias="enrollmentTarget", default=None,)
	lastAppSyncDateTime: Optional[datetime] = Field(alias="lastAppSyncDateTime", default=None,)
	lastAppSyncStatus: Optional[AndroidForWorkSyncStatus | str] = Field(alias="lastAppSyncStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	ownerOrganizationName: Optional[str] = Field(alias="ownerOrganizationName", default=None,)
	ownerUserPrincipalName: Optional[str] = Field(alias="ownerUserPrincipalName", default=None,)
	targetGroupIds: Optional[list[str]] = Field(alias="targetGroupIds", default=None,)

from .android_for_work_bind_status import AndroidForWorkBindStatus
from .android_for_work_enrollment_target import AndroidForWorkEnrollmentTarget
from .android_for_work_sync_status import AndroidForWorkSyncStatus
