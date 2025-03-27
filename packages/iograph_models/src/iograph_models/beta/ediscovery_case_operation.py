from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCaseOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	action: Optional[EdiscoveryCaseAction | str] = Field(alias="action", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[EdiscoveryCaseOperationStatus | str] = Field(alias="status", default=None,)

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
			if mapping_key == "#microsoft.graph.ediscovery.addToReviewSetOperation":
				from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
				return EdiscoveryAddToReviewSetOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseExportOperation":
				from .ediscovery_case_export_operation import EdiscoveryCaseExportOperation
				return EdiscoveryCaseExportOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseHoldOperation":
				from .ediscovery_case_hold_operation import EdiscoveryCaseHoldOperation
				return EdiscoveryCaseHoldOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.caseIndexOperation":
				from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
				return EdiscoveryCaseIndexOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.estimateStatisticsOperation":
				from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation
				return EdiscoveryEstimateStatisticsOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.purgeDataOperation":
				from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
				return EdiscoveryPurgeDataOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.ediscovery.tagOperation":
				from .ediscovery_tag_operation import EdiscoveryTagOperation
				return EdiscoveryTagOperation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .ediscovery_case_action import EdiscoveryCaseAction
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .result_info import ResultInfo
from .ediscovery_case_operation_status import EdiscoveryCaseOperationStatus

