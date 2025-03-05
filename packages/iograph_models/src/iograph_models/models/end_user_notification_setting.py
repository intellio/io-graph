from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class EndUserNotificationSetting(BaseModel):
	notificationPreference: Optional[EndUserNotificationPreference] = Field(default=None,alias="notificationPreference",)
	positiveReinforcement: Optional[PositiveReinforcementNotification] = Field(default=None,alias="positiveReinforcement",)
	settingType: Optional[EndUserNotificationSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.noTrainingNotificationSetting":
				from .no_training_notification_setting import NoTrainingNotificationSetting
				return NoTrainingNotificationSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.trainingNotificationSetting":
				from .training_notification_setting import TrainingNotificationSetting
				return TrainingNotificationSetting.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .end_user_notification_preference import EndUserNotificationPreference
from .positive_reinforcement_notification import PositiveReinforcementNotification
from .end_user_notification_setting_type import EndUserNotificationSettingType

