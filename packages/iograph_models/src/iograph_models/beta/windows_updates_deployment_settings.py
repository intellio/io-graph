from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDeploymentSettings(BaseModel):
	contentApplicability: Optional[WindowsUpdatesContentApplicabilitySettings] = Field(alias="contentApplicability", default=None,)
	expedite: Optional[WindowsUpdatesExpediteSettings] = Field(alias="expedite", default=None,)
	monitoring: Optional[WindowsUpdatesMonitoringSettings] = Field(alias="monitoring", default=None,)
	schedule: Optional[WindowsUpdatesScheduleSettings] = Field(alias="schedule", default=None,)
	userExperience: Optional[WindowsUpdatesUserExperienceSettings] = Field(alias="userExperience", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_content_applicability_settings import WindowsUpdatesContentApplicabilitySettings
from .windows_updates_expedite_settings import WindowsUpdatesExpediteSettings
from .windows_updates_monitoring_settings import WindowsUpdatesMonitoringSettings
from .windows_updates_schedule_settings import WindowsUpdatesScheduleSettings
from .windows_updates_user_experience_settings import WindowsUpdatesUserExperienceSettings

