from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(alias="applicationVersion",default=None,)
	headerValue: Optional[str] = Field(alias="headerValue",default=None,)
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
			if mapping_key == "#microsoft.graph.callRecords.clientUserAgent":
				from .call_records_client_user_agent import CallRecordsClientUserAgent
				return CallRecordsClientUserAgent.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.serviceUserAgent":
				from .call_records_service_user_agent import CallRecordsServiceUserAgent
				return CallRecordsServiceUserAgent.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


