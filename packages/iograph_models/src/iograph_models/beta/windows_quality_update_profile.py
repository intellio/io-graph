from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsQualityUpdateProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deployableContentDisplayName: Optional[str] = Field(alias="deployableContentDisplayName",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	expeditedUpdateSettings: Optional[ExpeditedWindowsQualityUpdateSettings] = Field(alias="expeditedUpdateSettings",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	releaseDateDisplayName: Optional[str] = Field(alias="releaseDateDisplayName",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	assignments: Optional[list[WindowsQualityUpdateProfileAssignment]] = Field(alias="assignments",default=None,)

from .expedited_windows_quality_update_settings import ExpeditedWindowsQualityUpdateSettings
from .windows_quality_update_profile_assignment import WindowsQualityUpdateProfileAssignment

