from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.partners.billing.exportSuccessOperation":
				from .partners_billing_export_success_operation import PartnersBillingExportSuccessOperation
				return PartnersBillingExportSuccessOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.failedOperation":
				from .partners_billing_failed_operation import PartnersBillingFailedOperation
				return PartnersBillingFailedOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.partners.billing.runningOperation":
				from .partners_billing_running_operation import PartnersBillingRunningOperation
				return PartnersBillingRunningOperation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .long_running_operation_status import LongRunningOperationStatus

