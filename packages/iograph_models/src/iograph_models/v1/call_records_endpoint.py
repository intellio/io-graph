from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class CallRecordsEndpoint(BaseModel):
	userAgent: Optional[Union[CallRecordsClientUserAgent, CallRecordsServiceUserAgent]] = Field(alias="userAgent", default=None,discriminator="odata_type", )
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
			if mapping_key == "#microsoft.graph.callRecords.participantEndpoint":
				from .call_records_participant_endpoint import CallRecordsParticipantEndpoint
				return CallRecordsParticipantEndpoint.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.serviceEndpoint":
				from .call_records_service_endpoint import CallRecordsServiceEndpoint
				return CallRecordsServiceEndpoint.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .call_records_client_user_agent import CallRecordsClientUserAgent
from .call_records_service_user_agent import CallRecordsServiceUserAgent
