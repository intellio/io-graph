from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DelegatedAdminRelationshipOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	data: Optional[str] = Field(default=None,alias="data",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	operationType: Optional[DelegatedAdminRelationshipOperationType] = Field(default=None,alias="operationType",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)

from .delegated_admin_relationship_operation_type import DelegatedAdminRelationshipOperationType
from .long_running_operation_status import LongRunningOperationStatus

