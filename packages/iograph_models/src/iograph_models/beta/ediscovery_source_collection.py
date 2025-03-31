from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class EdiscoverySourceCollection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ediscovery.sourceCollection"] = Field(alias="@odata.type",)
	contentQuery: Optional[str] = Field(alias="contentQuery", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dataSourceScopes: Optional[EdiscoveryDataSourceScopes | str] = Field(alias="dataSourceScopes", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	additionalSources: Optional[list[Annotated[Union[EdiscoverySiteSource, EdiscoveryUnifiedGroupSource, EdiscoveryUserSource],Field(discriminator="odata_type")]]] = Field(alias="additionalSources", default=None,)
	addToReviewSetOperation: Optional[EdiscoveryAddToReviewSetOperation] = Field(alias="addToReviewSetOperation", default=None,)
	custodianSources: Optional[list[Annotated[Union[EdiscoverySiteSource, EdiscoveryUnifiedGroupSource, EdiscoveryUserSource],Field(discriminator="odata_type")]]] = Field(alias="custodianSources", default=None,)
	lastEstimateStatisticsOperation: Optional[EdiscoveryEstimateStatisticsOperation] = Field(alias="lastEstimateStatisticsOperation", default=None,)
	noncustodialSources: Optional[list[EdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialSources", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ediscovery_data_source_scopes import EdiscoveryDataSourceScopes
from .ediscovery_site_source import EdiscoverySiteSource
from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
from .ediscovery_user_source import EdiscoveryUserSource
from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation
from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
