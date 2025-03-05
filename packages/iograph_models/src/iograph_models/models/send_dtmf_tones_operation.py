from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SendDtmfTonesOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo",default=None,)
	status: Optional[str | OperationStatus] = Field(alias="status",default=None,)
	completionReason: Optional[str | SendDtmfCompletionReason] = Field(alias="completionReason",default=None,)

from .result_info import ResultInfo
from .operation_status import OperationStatus
from .send_dtmf_completion_reason import SendDtmfCompletionReason

