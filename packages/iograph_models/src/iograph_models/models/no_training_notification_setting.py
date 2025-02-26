from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NoTrainingNotificationSetting(BaseModel):
	notificationPreference: Optional[EndUserNotificationPreference] = Field(default=None,alias="notificationPreference",)
	positiveReinforcement: Optional[PositiveReinforcementNotification] = Field(default=None,alias="positiveReinforcement",)
	settingType: Optional[EndUserNotificationSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	simulationNotification: Optional[SimulationNotification] = Field(default=None,alias="simulationNotification",)

from .end_user_notification_preference import EndUserNotificationPreference
from .positive_reinforcement_notification import PositiveReinforcementNotification
from .end_user_notification_setting_type import EndUserNotificationSettingType
from .simulation_notification import SimulationNotification

