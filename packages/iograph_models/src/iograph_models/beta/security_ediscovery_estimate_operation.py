from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryEstimateOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[SecurityCaseAction | str] = Field(alias="action",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status",default=None,)
	indexedItemCount: Optional[int] = Field(alias="indexedItemCount",default=None,)
	indexedItemsSize: Optional[int] = Field(alias="indexedItemsSize",default=None,)
	mailboxCount: Optional[int] = Field(alias="mailboxCount",default=None,)
	siteCount: Optional[int] = Field(alias="siteCount",default=None,)
	statisticsOptions: Optional[SecurityStatisticsOptions | str] = Field(alias="statisticsOptions",default=None,)
	unindexedItemCount: Optional[int] = Field(alias="unindexedItemCount",default=None,)
	unindexedItemsSize: Optional[int] = Field(alias="unindexedItemsSize",default=None,)
	search: Optional[SecurityEdiscoverySearch] = Field(alias="search",default=None,)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_statistics_options import SecurityStatisticsOptions
from .security_ediscovery_search import SecurityEdiscoverySearch

