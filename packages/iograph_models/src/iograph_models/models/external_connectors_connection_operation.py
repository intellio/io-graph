from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsConnectionOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	status: Optional[str | ExternalConnectorsConnectionOperationStatus] = Field(alias="status",default=None,)

from .public_error import PublicError
from .external_connectors_connection_operation_status import ExternalConnectorsConnectionOperationStatus

