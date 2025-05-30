from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class IndustryDataIndustryDataConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	sourceSystem: Optional[IndustryDataSourceSystemDefinition] = Field(alias="sourceSystem", default=None,)

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
			if mapping_key == "#microsoft.graph.industryData.oneRosterApiDataConnector":
				from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector
				return IndustryDataOneRosterApiDataConnector.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.azureDataLakeConnector":
				from .industry_data_azure_data_lake_connector import IndustryDataAzureDataLakeConnector
				return IndustryDataAzureDataLakeConnector.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
