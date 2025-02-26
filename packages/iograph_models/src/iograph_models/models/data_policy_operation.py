from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DataPolicyOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	progress: Optional[float] | Optional[str] | ReferenceNumeric
	status: Optional[DataPolicyOperationStatus] = Field(default=None,alias="status",)
	storageLocation: Optional[str] = Field(default=None,alias="storageLocation",)
	submittedDateTime: Optional[datetime] = Field(default=None,alias="submittedDateTime",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .reference_numeric import ReferenceNumeric
from .data_policy_operation_status import DataPolicyOperationStatus

