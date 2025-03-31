from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AccessReviewSettings(BaseModel):
	accessRecommendationsEnabled: Optional[bool] = Field(alias="accessRecommendationsEnabled", default=None,)
	activityDurationInDays: Optional[int] = Field(alias="activityDurationInDays", default=None,)
	autoApplyReviewResultsEnabled: Optional[bool] = Field(alias="autoApplyReviewResultsEnabled", default=None,)
	autoReviewEnabled: Optional[bool] = Field(alias="autoReviewEnabled", default=None,)
	autoReviewSettings: Optional[AutoReviewSettings] = Field(alias="autoReviewSettings", default=None,)
	justificationRequiredOnApproval: Optional[bool] = Field(alias="justificationRequiredOnApproval", default=None,)
	mailNotificationsEnabled: Optional[bool] = Field(alias="mailNotificationsEnabled", default=None,)
	recurrenceSettings: Optional[AccessReviewRecurrenceSettings] = Field(alias="recurrenceSettings", default=None,)
	remindersEnabled: Optional[bool] = Field(alias="remindersEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.businessFlowSettings":
				from .business_flow_settings import BusinessFlowSettings
				return BusinessFlowSettings.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .auto_review_settings import AutoReviewSettings
from .access_review_recurrence_settings import AccessReviewRecurrenceSettings
