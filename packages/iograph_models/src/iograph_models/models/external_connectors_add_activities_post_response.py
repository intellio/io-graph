from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class External_connectors_add_activitiesPostResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ExternalConnectorsExternalActivityResult] = Field(alias="value",)

from .external_connectors_external_activity_result import ExternalConnectorsExternalActivityResult

