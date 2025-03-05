from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class BaseEndUserNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage",default=None,)
	endUserNotification: Optional[EndUserNotification] = Field(alias="endUserNotification",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.positiveReinforcementNotification":
				from .positive_reinforcement_notification import PositiveReinforcementNotification
				return PositiveReinforcementNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.simulationNotification":
				from .simulation_notification import SimulationNotification
				return SimulationNotification.model_validate(data)
			if mapping_key == "#microsoft.graph.trainingReminderNotification":
				from .training_reminder_notification import TrainingReminderNotification
				return TrainingReminderNotification.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .end_user_notification import EndUserNotification

