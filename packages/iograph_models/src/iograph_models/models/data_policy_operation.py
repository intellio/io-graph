from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DataPolicyOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	progress: float | str | ReferenceNumeric
	status: Optional[DataPolicyOperationStatus | str] = Field(alias="status",default=None,)
	storageLocation: Optional[str] = Field(alias="storageLocation",default=None,)
	submittedDateTime: Optional[datetime] = Field(alias="submittedDateTime",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)

from .reference_numeric import ReferenceNumeric
from .data_policy_operation_status import DataPolicyOperationStatus

