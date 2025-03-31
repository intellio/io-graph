from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class TrainingNotificationSetting(BaseModel):
	notificationPreference: Optional[EndUserNotificationPreference | str] = Field(alias="notificationPreference", default=None,)
	positiveReinforcement: Optional[PositiveReinforcementNotification] = Field(alias="positiveReinforcement", default=None,)
	settingType: Optional[EndUserNotificationSettingType | str] = Field(alias="settingType", default=None,)
	odata_type: Literal["#microsoft.graph.trainingNotificationSetting"] = Field(alias="@odata.type", default="#microsoft.graph.trainingNotificationSetting")
	trainingAssignment: Optional[Union[PositiveReinforcementNotification, SimulationNotification, TrainingReminderNotification]] = Field(alias="trainingAssignment", default=None,discriminator="odata_type", )
	trainingReminder: Optional[TrainingReminderNotification] = Field(alias="trainingReminder", default=None,)

from .end_user_notification_preference import EndUserNotificationPreference
from .positive_reinforcement_notification import PositiveReinforcementNotification
from .end_user_notification_setting_type import EndUserNotificationSettingType
from .simulation_notification import SimulationNotification
from .training_reminder_notification import TrainingReminderNotification
