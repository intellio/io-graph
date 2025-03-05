from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LongRunningOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation",default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status",default=None,)
	statusDetail: Optional[str] = Field(alias="statusDetail",default=None,)

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

