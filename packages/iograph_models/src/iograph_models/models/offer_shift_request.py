from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class OfferShiftRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	assignedTo: Optional[ScheduleChangeRequestActor] = Field(default=None,alias="assignedTo",)
	managerActionDateTime: Optional[datetime] = Field(default=None,alias="managerActionDateTime",)
	managerActionMessage: Optional[str] = Field(default=None,alias="managerActionMessage",)
	managerUserId: Optional[str] = Field(default=None,alias="managerUserId",)
	senderDateTime: Optional[datetime] = Field(default=None,alias="senderDateTime",)
	senderMessage: Optional[str] = Field(default=None,alias="senderMessage",)
	senderUserId: Optional[str] = Field(default=None,alias="senderUserId",)
	state: Optional[ScheduleChangeState] = Field(default=None,alias="state",)
	recipientActionDateTime: Optional[datetime] = Field(default=None,alias="recipientActionDateTime",)
	recipientActionMessage: Optional[str] = Field(default=None,alias="recipientActionMessage",)
	recipientUserId: Optional[str] = Field(default=None,alias="recipientUserId",)
	senderShiftId: Optional[str] = Field(default=None,alias="senderShiftId",)

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
			if mapping_key == "#microsoft.graph.swapShiftsChangeRequest":
				from .swap_shifts_change_request import SwapShiftsChangeRequest
				return SwapShiftsChangeRequest.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .schedule_change_request_actor import ScheduleChangeRequestActor
from .schedule_change_state import ScheduleChangeState

