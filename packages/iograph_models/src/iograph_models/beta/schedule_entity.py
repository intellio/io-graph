from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ScheduleEntity(BaseModel):
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	theme: Optional[ScheduleEntityTheme | str] = Field(alias="theme", default=None,)
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
			if mapping_key == "#microsoft.graph.shiftItem":
				from .shift_item import ShiftItem
				return ShiftItem.model_validate(data)
			if mapping_key == "#microsoft.graph.openShiftItem":
				from .open_shift_item import OpenShiftItem
				return OpenShiftItem.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOffItem":
				from .time_off_item import TimeOffItem
				return TimeOffItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .schedule_entity_theme import ScheduleEntityTheme

