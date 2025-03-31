from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class IndustryDataOAuthClientCredential(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isValid: Optional[bool] = Field(alias="isValid", default=None,)
	lastValidDateTime: Optional[datetime] = Field(alias="lastValidDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.oAuthClientCredential"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.oAuthClientCredential")
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret", default=None,)

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
			if mapping_key == "#microsoft.graph.industryData.oAuth1ClientCredential":
				from .industry_data_o_auth1_client_credential import IndustryDataOAuth1ClientCredential
				return IndustryDataOAuth1ClientCredential.model_validate(data)
			if mapping_key == "#microsoft.graph.industryData.oAuth2ClientCredential":
				from .industry_data_o_auth2_client_credential import IndustryDataOAuth2ClientCredential
				return IndustryDataOAuth2ClientCredential.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

