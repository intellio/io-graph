from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataActivityStatistics(BaseModel):
	activityId: Optional[str] = Field(alias="activityId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	status: Optional[IndustryDataIndustryDataActivityStatus | str] = Field(alias="status", default=None,)
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
			if mapping_key == "#microsoft.graph.industryData.inboundActivityResults":
				from .industry_data_inbound_activity_results import IndustryDataInboundActivityResults
				return IndustryDataInboundActivityResults.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .industry_data_industry_data_activity_status import IndustryDataIndustryDataActivityStatus

