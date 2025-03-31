from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class IndustryDataIndustryDataRunActivity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	blockingError: Optional[PublicError] = Field(alias="blockingError", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	status: Optional[IndustryDataIndustryDataActivityStatus | str] = Field(alias="status", default=None,)
	activity: Optional[Union[IndustryDataInboundApiFlow, IndustryDataInboundFileFlow]] = Field(alias="activity", default=None,discriminator="odata_type", )

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
			if mapping_key == "#microsoft.graph.industryData.inboundFlowActivity":
				from .industry_data_inbound_flow_activity import IndustryDataInboundFlowActivity
				return IndustryDataInboundFlowActivity.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.outboundFlowActivity":
				from .industry_data_outbound_flow_activity import IndustryDataOutboundFlowActivity
				return IndustryDataOutboundFlowActivity.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .public_error import PublicError
from .industry_data_industry_data_activity_status import IndustryDataIndustryDataActivityStatus
from .industry_data_inbound_api_flow import IndustryDataInboundApiFlow
from .industry_data_inbound_file_flow import IndustryDataInboundFileFlow
