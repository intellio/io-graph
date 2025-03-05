from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsConnectionOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	status: Optional[ExternalConnectorsConnectionOperationStatus] = Field(default=None,alias="status",)

from .public_error import PublicError
from .external_connectors_connection_operation_status import ExternalConnectorsConnectionOperationStatus

