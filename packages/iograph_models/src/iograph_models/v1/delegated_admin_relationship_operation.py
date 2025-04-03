from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminRelationshipOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.delegatedAdminRelationshipOperation"] = Field(alias="@odata.type", default="#microsoft.graph.delegatedAdminRelationshipOperation")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	data: Optional[str] = Field(alias="data", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	operationType: Optional[DelegatedAdminRelationshipOperationType | str] = Field(alias="operationType", default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status", default=None,)

from .delegated_admin_relationship_operation_type import DelegatedAdminRelationshipOperationType
from .long_running_operation_status import LongRunningOperationStatus
