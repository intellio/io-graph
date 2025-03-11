from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsCallLogRow(BaseModel):
	administrativeUnitInfos: Optional[list[CallRecordsAdministrativeUnitInfo]] = Field(alias="administrativeUnitInfos",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	otherPartyCountryCode: Optional[str] = Field(alias="otherPartyCountryCode",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
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
			if mapping_key == "#microsoft.graph.callRecords.directRoutingLogRow":
				from .call_records_direct_routing_log_row import CallRecordsDirectRoutingLogRow
				return CallRecordsDirectRoutingLogRow.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.pstnCallLogRow":
				from .call_records_pstn_call_log_row import CallRecordsPstnCallLogRow
				return CallRecordsPstnCallLogRow.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecords.smsLogRow":
				from .call_records_sms_log_row import CallRecordsSmsLogRow
				return CallRecordsSmsLogRow.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .call_records_administrative_unit_info import CallRecordsAdministrativeUnitInfo

