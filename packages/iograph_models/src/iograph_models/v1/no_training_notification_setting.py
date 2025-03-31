from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NoTrainingNotificationSetting(BaseModel):
	notificationPreference: Optional[EndUserNotificationPreference | str] = Field(alias="notificationPreference", default=None,)
	positiveReinforcement: Optional[PositiveReinforcementNotification] = Field(alias="positiveReinforcement", default=None,)
	settingType: Optional[EndUserNotificationSettingType | str] = Field(alias="settingType", default=None,)
	odata_type: Literal["#microsoft.graph.noTrainingNotificationSetting"] = Field(alias="@odata.type", default="#microsoft.graph.noTrainingNotificationSetting")
	simulationNotification: Optional[SimulationNotification] = Field(alias="simulationNotification", default=None,)

from .end_user_notification_preference import EndUserNotificationPreference
from .positive_reinforcement_notification import PositiveReinforcementNotification
from .end_user_notification_setting_type import EndUserNotificationSettingType
from .simulation_notification import SimulationNotification
