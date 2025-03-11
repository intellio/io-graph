from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataActivity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus",default=None,)

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
			if mapping_key == "#microsoft.graph.industryData.inboundFlow":
				from .industry_data_inbound_flow import IndustryDataInboundFlow
				return IndustryDataInboundFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.inboundApiFlow":
				from .industry_data_inbound_api_flow import IndustryDataInboundApiFlow
				return IndustryDataInboundApiFlow.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.inboundFileFlow":
				from .industry_data_inbound_file_flow import IndustryDataInboundFileFlow
				return IndustryDataInboundFileFlow.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .industry_data_readiness_status import IndustryDataReadinessStatus

