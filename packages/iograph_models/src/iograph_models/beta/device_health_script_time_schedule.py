from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceHealthScriptTimeSchedule(BaseModel):
	interval: Optional[int] = Field(alias="interval", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptTimeSchedule"] = Field(alias="@odata.type", default="#microsoft.graph.deviceHealthScriptTimeSchedule")
	time: Optional[str] = Field(alias="time", default=None,)
	useUtc: Optional[bool] = Field(alias="useUtc", default=None,)

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
			if mapping_key == "#microsoft.graph.deviceHealthScriptDailySchedule":
				from .device_health_script_daily_schedule import DeviceHealthScriptDailySchedule
				return DeviceHealthScriptDailySchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptRunOnceSchedule":
				from .device_health_script_run_once_schedule import DeviceHealthScriptRunOnceSchedule
				return DeviceHealthScriptRunOnceSchedule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

