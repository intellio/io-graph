from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SendDtmfTonesOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)
	resultInfo: Optional[ResultInfo] = Field(default=None,alias="resultInfo",)
	status: Optional[OperationStatus] = Field(default=None,alias="status",)
	completionReason: Optional[SendDtmfCompletionReason] = Field(default=None,alias="completionReason",)

from .result_info import ResultInfo
from .operation_status import OperationStatus
from .send_dtmf_completion_reason import SendDtmfCompletionReason

