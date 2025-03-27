from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ActivityStatistics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activity: Optional[AnalyticsActivityType | str] = Field(alias="activity", default=None,)
	duration: Optional[str] = Field(alias="duration", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	timeZoneUsed: Optional[str] = Field(alias="timeZoneUsed", default=None,)

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
			if mapping_key == "#microsoft.graph.callActivityStatistics":
				from .call_activity_statistics import CallActivityStatistics
				return CallActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.chatActivityStatistics":
				from .chat_activity_statistics import ChatActivityStatistics
				return ChatActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.emailActivityStatistics":
				from .email_activity_statistics import EmailActivityStatistics
				return EmailActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.focusActivityStatistics":
				from .focus_activity_statistics import FocusActivityStatistics
				return FocusActivityStatistics.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingActivityStatistics":
				from .meeting_activity_statistics import MeetingActivityStatistics
				return MeetingActivityStatistics.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .analytics_activity_type import AnalyticsActivityType

