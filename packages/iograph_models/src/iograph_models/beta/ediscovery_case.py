from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryCase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	closedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="closedBy", default=None,discriminator="odata_type", )
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[EdiscoveryCaseStatus | str] = Field(alias="status", default=None,)
	custodians: Optional[list[EdiscoveryCustodian]] = Field(alias="custodians", default=None,)
	legalHolds: Optional[list[EdiscoveryLegalHold]] = Field(alias="legalHolds", default=None,)
	noncustodialDataSources: Optional[list[EdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialDataSources", default=None,)
	operations: Optional[list[Annotated[Union[EdiscoveryAddToReviewSetOperation, EdiscoveryCaseExportOperation, EdiscoveryCaseHoldOperation, EdiscoveryCaseIndexOperation, EdiscoveryEstimateStatisticsOperation, EdiscoveryPurgeDataOperation, EdiscoveryTagOperation]],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	reviewSets: Optional[list[EdiscoveryReviewSet]] = Field(alias="reviewSets", default=None,)
	settings: Optional[EdiscoveryCaseSettings] = Field(alias="settings", default=None,)
	sourceCollections: Optional[list[EdiscoverySourceCollection]] = Field(alias="sourceCollections", default=None,)
	tags: Optional[list[EdiscoveryTag]] = Field(alias="tags", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ediscovery_case_status import EdiscoveryCaseStatus
from .ediscovery_custodian import EdiscoveryCustodian
from .ediscovery_legal_hold import EdiscoveryLegalHold
from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
from .ediscovery_case_export_operation import EdiscoveryCaseExportOperation
from .ediscovery_case_hold_operation import EdiscoveryCaseHoldOperation
from .ediscovery_case_index_operation import EdiscoveryCaseIndexOperation
from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation
from .ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
from .ediscovery_tag_operation import EdiscoveryTagOperation
from .ediscovery_review_set import EdiscoveryReviewSet
from .ediscovery_case_settings import EdiscoveryCaseSettings
from .ediscovery_source_collection import EdiscoverySourceCollection
from .ediscovery_tag import EdiscoveryTag

