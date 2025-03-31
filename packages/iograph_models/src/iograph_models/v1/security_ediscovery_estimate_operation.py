from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoveryEstimateOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoveryEstimateOperation"] = Field(alias="@odata.type",)
	action: Optional[SecurityCaseAction | str] = Field(alias="action", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status", default=None,)
	indexedItemCount: Optional[int] = Field(alias="indexedItemCount", default=None,)
	indexedItemsSize: Optional[int] = Field(alias="indexedItemsSize", default=None,)
	mailboxCount: Optional[int] = Field(alias="mailboxCount", default=None,)
	siteCount: Optional[int] = Field(alias="siteCount", default=None,)
	unindexedItemCount: Optional[int] = Field(alias="unindexedItemCount", default=None,)
	unindexedItemsSize: Optional[int] = Field(alias="unindexedItemsSize", default=None,)
	search: Optional[SecurityEdiscoverySearch] = Field(alias="search", default=None,)

from .security_case_action import SecurityCaseAction
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_ediscovery_search import SecurityEdiscoverySearch
