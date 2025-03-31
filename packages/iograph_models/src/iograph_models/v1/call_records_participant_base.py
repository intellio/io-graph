from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class CallRecordsParticipantBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	administrativeUnitInfos: Optional[list[CallRecordsAdministrativeUnitInfo]] = Field(alias="administrativeUnitInfos", default=None,)
	identity: Optional[CommunicationsIdentitySet] = Field(alias="identity", default=None,)

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
			if mapping_key == "#microsoft.graph.callRecords.organizer":
				from .call_records_organizer import CallRecordsOrganizer
				return CallRecordsOrganizer.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.participant":
				from .call_records_participant import CallRecordsParticipant
				return CallRecordsParticipant.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo
from .communications_identity_set import CommunicationsIdentitySet
