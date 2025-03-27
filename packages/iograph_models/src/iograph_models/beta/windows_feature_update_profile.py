from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsFeatureUpdateProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deployableContentDisplayName: Optional[str] = Field(alias="deployableContentDisplayName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endOfSupportDate: Optional[datetime] = Field(alias="endOfSupportDate", default=None,)
	featureUpdateVersion: Optional[str] = Field(alias="featureUpdateVersion", default=None,)
	installFeatureUpdatesOptional: Optional[bool] = Field(alias="installFeatureUpdatesOptional", default=None,)
	installLatestWindows10OnWindows11IneligibleDevice: Optional[bool] = Field(alias="installLatestWindows10OnWindows11IneligibleDevice", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	rolloutSettings: Optional[WindowsUpdateRolloutSettings] = Field(alias="rolloutSettings", default=None,)
	assignments: Optional[list[WindowsFeatureUpdateProfileAssignment]] = Field(alias="assignments", default=None,)

from .windows_update_rollout_settings import WindowsUpdateRolloutSettings
from .windows_feature_update_profile_assignment import WindowsFeatureUpdateProfileAssignment

