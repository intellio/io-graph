from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingNotificationSetting(BaseModel):
	notificationPreference: Optional[EndUserNotificationPreference] = Field(default=None,alias="notificationPreference",)
	positiveReinforcement: Optional[PositiveReinforcementNotification] = Field(default=None,alias="positiveReinforcement",)
	settingType: Optional[EndUserNotificationSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	trainingAssignment: SerializeAsAny[Optional[BaseEndUserNotification]] = Field(default=None,alias="trainingAssignment",)
	trainingReminder: Optional[TrainingReminderNotification] = Field(default=None,alias="trainingReminder",)

from .end_user_notification_preference import EndUserNotificationPreference
from .positive_reinforcement_notification import PositiveReinforcementNotification
from .end_user_notification_setting_type import EndUserNotificationSettingType
from .base_end_user_notification import BaseEndUserNotification
from .training_reminder_notification import TrainingReminderNotification

