from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataApiDataConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.apiDataConnector"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.apiDataConnector")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	sourceSystem: Optional[IndustryDataSourceSystemDefinition] = Field(alias="sourceSystem", default=None,)
	apiFormat: Optional[IndustryDataApiFormat | str] = Field(alias="apiFormat", default=None,)
	baseUrl: Optional[str] = Field(alias="baseUrl", default=None,)
	credential: Optional[Union[IndustryDataOAuthClientCredential, IndustryDataOAuth1ClientCredential, IndustryDataOAuth2ClientCredential]] = Field(alias="credential", default=None,discriminator="odata_type", )

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
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
from .industry_data_api_format import IndustryDataApiFormat
from .industry_data_o_auth_client_credential import IndustryDataOAuthClientCredential
from .industry_data_o_auth1_client_credential import IndustryDataOAuth1ClientCredential
from .industry_data_o_auth2_client_credential import IndustryDataOAuth2ClientCredential

