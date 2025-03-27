from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataInboundFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.inboundFlow"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.inboundFlow")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus", default=None,)
	dataDomain: Optional[IndustryDataInboundDomain | str] = Field(alias="dataDomain", default=None,)
	effectiveDateTime: Optional[datetime] = Field(alias="effectiveDateTime", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	dataConnector: Optional[Union[IndustryDataApiDataConnector, IndustryDataOneRosterApiDataConnector, IndustryDataFileDataConnector, IndustryDataAzureDataLakeConnector]] = Field(alias="dataConnector", default=None,discriminator="odata_type", )
	year: Optional[IndustryDataYearTimePeriodDefinition] = Field(alias="year", default=None,)

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
from .industry_data_inbound_domain import IndustryDataInboundDomain
from .industry_data_api_data_connector import IndustryDataApiDataConnector
from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector
from .industry_data_file_data_connector import IndustryDataFileDataConnector
from .industry_data_azure_data_lake_connector import IndustryDataAzureDataLakeConnector
from .industry_data_year_time_period_definition import IndustryDataYearTimePeriodDefinition

