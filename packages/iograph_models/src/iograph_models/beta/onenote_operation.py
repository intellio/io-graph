from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OnenoteOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onenoteOperation"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)
	error: Optional[OnenoteOperationError] = Field(alias="error", default=None,)
	percentComplete: Optional[str] = Field(alias="percentComplete", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)

from .operation_status import OperationStatus
from .onenote_operation_error import OnenoteOperationError
