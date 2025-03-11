from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecordOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status",default=None,)
	completionReason: Optional[RecordCompletionReason | str] = Field(alias="completionReason",default=None,)
	recordingAccessToken: Optional[str] = Field(alias="recordingAccessToken",default=None,)
	recordingLocation: Optional[str] = Field(alias="recordingLocation",default=None,)

from .result_info import ResultInfo
from .operation_status import OperationStatus
from .record_completion_reason import RecordCompletionReason

