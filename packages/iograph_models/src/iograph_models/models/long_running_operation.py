from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class LongRunningOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	resourceLocation: Optional[str] = Field(default=None,alias="resourceLocation",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)
	statusDetail: Optional[str] = Field(default=None,alias="statusDetail",)

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
			if mapping_key == "#microsoft.graph.attackSimulationOperation":
				from .attack_simulation_operation import AttackSimulationOperation
				return AttackSimulationOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.engagementAsyncOperation":
				from .engagement_async_operation import EngagementAsyncOperation
				return EngagementAsyncOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.richLongRunningOperation":
				from .rich_long_running_operation import RichLongRunningOperation
				return RichLongRunningOperation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .long_running_operation_status import LongRunningOperationStatus

