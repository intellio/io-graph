from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType] = Field(default=None,alias="settingType",)
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
			if mapping_key == "#microsoft.graph.customTrainingSetting":
				from .custom_training_setting import CustomTrainingSetting
				return CustomTrainingSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftCustomTrainingSetting":
				from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting
				return MicrosoftCustomTrainingSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftManagedTrainingSetting":
				from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting
				return MicrosoftManagedTrainingSetting.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftTrainingAssignmentMapping":
				from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
				return MicrosoftTrainingAssignmentMapping.model_validate(data)
			if mapping_key == "#microsoft.graph.noTrainingSetting":
				from .no_training_setting import NoTrainingSetting
				return NoTrainingSetting.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .training_setting_type import TrainingSettingType

