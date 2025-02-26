from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsConnectionOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ExternalConnectorsConnectionOperation] = Field(alias="value",)

from .external_connectors_connection_operation import ExternalConnectorsConnectionOperation

