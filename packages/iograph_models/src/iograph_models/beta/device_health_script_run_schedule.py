from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptRunSchedule(BaseModel):
	interval: Optional[int] = Field(alias="interval",default=None,)
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
			if mapping_key == "#microsoft.graph.deviceHealthScriptHourlySchedule":
				from .device_health_script_hourly_schedule import DeviceHealthScriptHourlySchedule
				return DeviceHealthScriptHourlySchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptTimeSchedule":
				from .device_health_script_time_schedule import DeviceHealthScriptTimeSchedule
				return DeviceHealthScriptTimeSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptDailySchedule":
				from .device_health_script_daily_schedule import DeviceHealthScriptDailySchedule
				return DeviceHealthScriptDailySchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceHealthScriptRunOnceSchedule":
				from .device_health_script_run_once_schedule import DeviceHealthScriptRunOnceSchedule
				return DeviceHealthScriptRunOnceSchedule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


