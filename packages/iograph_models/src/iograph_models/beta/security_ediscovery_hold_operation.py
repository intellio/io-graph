from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryHoldOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[SecurityCaseAction | str] = Field(alias="action",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status",default=None,)

from .security_case_action import SecurityCaseAction
from .identity_set import IdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus

