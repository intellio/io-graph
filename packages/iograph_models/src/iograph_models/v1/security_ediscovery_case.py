from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryCase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoveryCase"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoveryCase")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[SecurityCaseStatus | str] = Field(alias="status", default=None,)
	closedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="closedBy", default=None,discriminator="odata_type", )
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	custodians: Optional[list[SecurityEdiscoveryCustodian]] = Field(alias="custodians", default=None,)
	noncustodialDataSources: Optional[list[SecurityEdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialDataSources", default=None,)
	operations: Optional[list[Annotated[Union[SecurityEdiscoveryAddToReviewSetOperation, SecurityEdiscoveryEstimateOperation, SecurityEdiscoveryExportOperation, SecurityEdiscoveryHoldOperation, SecurityEdiscoveryIndexOperation, SecurityEdiscoveryPurgeDataOperation, SecurityEdiscoverySearchExportOperation, SecurityEdiscoveryTagOperation]],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	reviewSets: Optional[list[SecurityEdiscoveryReviewSet]] = Field(alias="reviewSets", default=None,)
	searches: Optional[list[SecurityEdiscoverySearch]] = Field(alias="searches", default=None,)
	settings: Optional[SecurityEdiscoveryCaseSettings] = Field(alias="settings", default=None,)
	tags: Optional[list[SecurityEdiscoveryReviewTag]] = Field(alias="tags", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .security_case_status import SecurityCaseStatus
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .security_ediscovery_custodian import SecurityEdiscoveryCustodian
from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource
from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
from .security_ediscovery_export_operation import SecurityEdiscoveryExportOperation
from .security_ediscovery_hold_operation import SecurityEdiscoveryHoldOperation
from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation
from .security_ediscovery_purge_data_operation import SecurityEdiscoveryPurgeDataOperation
from .security_ediscovery_search_export_operation import SecurityEdiscoverySearchExportOperation
from .security_ediscovery_tag_operation import SecurityEdiscoveryTagOperation
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_search import SecurityEdiscoverySearch
from .security_ediscovery_case_settings import SecurityEdiscoveryCaseSettings
from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

