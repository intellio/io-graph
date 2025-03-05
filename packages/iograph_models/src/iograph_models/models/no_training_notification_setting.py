from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NoTrainingNotificationSetting(BaseModel):
	notificationPreference: Optional[str | EndUserNotificationPreference] = Field(alias="notificationPreference",default=None,)
	positiveReinforcement: Optional[PositiveReinforcementNotification] = Field(alias="positiveReinforcement",default=None,)
	settingType: Optional[str | EndUserNotificationSettingType] = Field(alias="settingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	simulationNotification: Optional[SimulationNotification] = Field(alias="simulationNotification",default=None,)

from .end_user_notification_preference import EndUserNotificationPreference
from .positive_reinforcement_notification import PositiveReinforcementNotification
from .end_user_notification_setting_type import EndUserNotificationSettingType
from .simulation_notification import SimulationNotification

