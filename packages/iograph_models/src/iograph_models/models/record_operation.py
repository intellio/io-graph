from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecordOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[OperationStatus] = Field(default=None,alias="status",)
	recordingAccessToken: Optional[str] = Field(default=None,alias="recordingAccessToken",)
	recordingLocation: Optional[str] = Field(default=None,alias="recordingLocation",)

from .result_info import ResultInfo
from .operation_status import OperationStatus

