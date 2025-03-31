from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SendDtmfTonesOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sendDtmfTonesOperation"] = Field(alias="@odata.type",)
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)
	completionReason: Optional[SendDtmfCompletionReason | str] = Field(alias="completionReason", default=None,)

from .result_info import ResultInfo
from .operation_status import OperationStatus
from .send_dtmf_completion_reason import SendDtmfCompletionReason
