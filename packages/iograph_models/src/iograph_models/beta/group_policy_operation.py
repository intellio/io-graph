from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyOperation"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyOperation")
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	operationStatus: Optional[GroupPolicyOperationStatus | str] = Field(alias="operationStatus", default=None,)
	operationType: Optional[GroupPolicyOperationType | str] = Field(alias="operationType", default=None,)
	statusDetails: Optional[str] = Field(alias="statusDetails", default=None,)

from .group_policy_operation_status import GroupPolicyOperationStatus
from .group_policy_operation_type import GroupPolicyOperationType
