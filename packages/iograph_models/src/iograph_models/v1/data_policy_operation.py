from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DataPolicyOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dataPolicyOperation"] = Field(alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	progress: float | str | ReferenceNumeric
	status: Optional[DataPolicyOperationStatus | str] = Field(alias="status", default=None,)
	storageLocation: Optional[str] = Field(alias="storageLocation", default=None,)
	submittedDateTime: Optional[datetime] = Field(alias="submittedDateTime", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .reference_numeric import ReferenceNumeric
from .data_policy_operation_status import DataPolicyOperationStatus
