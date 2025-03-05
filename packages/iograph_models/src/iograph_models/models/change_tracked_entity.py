from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeTrackedEntity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)

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
			if mapping_key == "#microsoft.graph.dayNote":
				from .day_note import DayNote
				return DayNote.model_validate(data)
			if mapping_key == "#microsoft.graph.openShift":
				from .open_shift import OpenShift
				return OpenShift.model_validate(data)
			if mapping_key == "#microsoft.graph.scheduleChangeRequest":
				from .schedule_change_request import ScheduleChangeRequest
				return ScheduleChangeRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.offerShiftRequest":
				from .offer_shift_request import OfferShiftRequest
				return OfferShiftRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.swapShiftsChangeRequest":
				from .swap_shifts_change_request import SwapShiftsChangeRequest
				return SwapShiftsChangeRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.openShiftChangeRequest":
				from .open_shift_change_request import OpenShiftChangeRequest
				return OpenShiftChangeRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOffRequest":
				from .time_off_request import TimeOffRequest
				return TimeOffRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.schedulingGroup":
				from .scheduling_group import SchedulingGroup
				return SchedulingGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.shift":
				from .shift import Shift
				return Shift.model_validate(data)
			if mapping_key == "#microsoft.graph.shiftPreferences":
				from .shift_preferences import ShiftPreferences
				return ShiftPreferences.model_validate(data)
			if mapping_key == "#microsoft.graph.timeCard":
				from .time_card import TimeCard
				return TimeCard.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOff":
				from .time_off import TimeOff
				return TimeOff.model_validate(data)
			if mapping_key == "#microsoft.graph.timeOffReason":
				from .time_off_reason import TimeOffReason
				return TimeOffReason.model_validate(data)
			if mapping_key == "#microsoft.graph.workforceIntegration":
				from .workforce_integration import WorkforceIntegration
				return WorkforceIntegration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .identity_set import IdentitySet

