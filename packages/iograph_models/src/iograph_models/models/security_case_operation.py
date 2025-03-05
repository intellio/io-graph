from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCaseOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	action: Optional[SecurityCaseAction] = Field(default=None,alias="action",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	percentProgress: Optional[int] = Field(default=None,alias="percentProgress",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[SecurityCaseOperationStatus] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation":
				from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
				return SecurityEdiscoveryAddToReviewSetOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryEstimateOperation":
				from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
				return SecurityEdiscoveryEstimateOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryExportOperation":
				from .security_ediscovery_export_operation import SecurityEdiscoveryExportOperation
				return SecurityEdiscoveryExportOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryHoldOperation":
				from .security_ediscovery_hold_operation import SecurityEdiscoveryHoldOperation
				return SecurityEdiscoveryHoldOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryIndexOperation":
				from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
				return SecurityEdiscoveryIndexOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryPurgeDataOperation":
				from .security_ediscovery_purge_data_operation import SecurityEdiscoveryPurgeDataOperation
				return SecurityEdiscoveryPurgeDataOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoverySearchExportOperation":
				from .security_ediscovery_search_export_operation import SecurityEdiscoverySearchExportOperation
				return SecurityEdiscoverySearchExportOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ediscoveryTagOperation":
				from .security_ediscovery_tag_operation import SecurityEdiscoveryTagOperation
				return SecurityEdiscoveryTagOperation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus

