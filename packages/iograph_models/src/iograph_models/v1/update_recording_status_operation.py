from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UpdateRecordingStatusOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.updateRecordingStatusOperation"] = Field(alias="@odata.type", default="#microsoft.graph.updateRecordingStatusOperation")
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)

from .result_info import ResultInfo
from .operation_status import OperationStatus
