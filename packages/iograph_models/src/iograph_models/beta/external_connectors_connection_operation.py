from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalConnectorsConnectionOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnectors.connectionOperation"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnectors.connectionOperation")
	error: Optional[PublicError] = Field(alias="error", default=None,)
	status: Optional[ExternalConnectorsConnectionOperationStatus | str] = Field(alias="status", default=None,)

from .public_error import PublicError
from .external_connectors_connection_operation_status import ExternalConnectorsConnectionOperationStatus
