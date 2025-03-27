from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class InactiveUsersByApplicationMetricBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	inactive30DayCount: Optional[int] = Field(alias="inactive30DayCount", default=None,)
	inactive60DayCount: Optional[int] = Field(alias="inactive60DayCount", default=None,)
	inactive90DayCount: Optional[int] = Field(alias="inactive90DayCount", default=None,)

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
			if mapping_key == "#microsoft.graph.dailyInactiveUsersByApplicationMetric":
				from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
				return DailyInactiveUsersByApplicationMetric.model_validate(data)
			if mapping_key == "#microsoft.graph.monthlyInactiveUsersByApplicationMetric":
				from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
				return MonthlyInactiveUsersByApplicationMetric.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


