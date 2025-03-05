from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ShiftItem(BaseModel):
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	theme: Optional[ScheduleEntityTheme] = Field(default=None,alias="theme",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activities: Optional[list[ShiftActivity]] = Field(default=None,alias="activities",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	notes: Optional[str] = Field(default=None,alias="notes",)

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
			if mapping_key == "#microsoft.graph.openShiftItem":
				from .open_shift_item import OpenShiftItem
				return OpenShiftItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .schedule_entity_theme import ScheduleEntityTheme
from .shift_activity import ShiftActivity

