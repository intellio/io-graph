from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ConnectionOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.connectionOperation"] = Field(alias="@odata.type", default="#microsoft.graph.connectionOperation")
	error: Optional[PublicError] = Field(alias="error", default=None,)
	status: Optional[ConnectionOperationStatus | str] = Field(alias="status", default=None,)

from .public_error import PublicError
from .connection_operation_status import ConnectionOperationStatus
