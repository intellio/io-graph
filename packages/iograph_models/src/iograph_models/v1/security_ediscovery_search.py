from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoverySearch(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoverySearch"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoverySearch")
	contentQuery: Optional[str] = Field(alias="contentQuery", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	dataSourceScopes: Optional[SecurityDataSourceScopes | str] = Field(alias="dataSourceScopes", default=None,)
	additionalSources: Optional[list[Annotated[Union[SecuritySiteSource, SecurityUnifiedGroupSource, SecurityUserSource],Field(discriminator="odata_type")]]] = Field(alias="additionalSources", default=None,)
	addToReviewSetOperation: Optional[SecurityEdiscoveryAddToReviewSetOperation] = Field(alias="addToReviewSetOperation", default=None,)
	custodianSources: Optional[list[Annotated[Union[SecuritySiteSource, SecurityUnifiedGroupSource, SecurityUserSource],Field(discriminator="odata_type")]]] = Field(alias="custodianSources", default=None,)
	lastEstimateStatisticsOperation: Optional[SecurityEdiscoveryEstimateOperation] = Field(alias="lastEstimateStatisticsOperation", default=None,)
	noncustodialSources: Optional[list[SecurityEdiscoveryNoncustodialDataSource]] = Field(alias="noncustodialSources", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .security_data_source_scopes import SecurityDataSourceScopes
from .security_site_source import SecuritySiteSource
from .security_unified_group_source import SecurityUnifiedGroupSource
from .security_user_source import SecurityUserSource
from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation
from .security_ediscovery_estimate_operation import SecurityEdiscoveryEstimateOperation
from .security_ediscovery_noncustodial_data_source import SecurityEdiscoveryNoncustodialDataSource
