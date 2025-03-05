from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryAddToReviewSetOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	action: Optional[SecurityCaseAction] = Field(default=None,alias="action",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	percentProgress: Optional[int] = Field(default=None,alias="percentProgress",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[SecurityCaseOperationStatus] = Field(default=None,alias="status",)
	reviewSet: Optional[SecurityEdiscoveryReviewSet] = Field(default=None,alias="reviewSet",)
	search: Optional[SecurityEdiscoverySearch] = Field(default=None,alias="search",)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_ediscovery_review_set import SecurityEdiscoveryReviewSet
from .security_ediscovery_search import SecurityEdiscoverySearch

