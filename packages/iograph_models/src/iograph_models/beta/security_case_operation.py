from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class SecurityCaseOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	action: Optional[SecurityCaseAction | str] = Field(alias="action", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status", default=None,)

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
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
