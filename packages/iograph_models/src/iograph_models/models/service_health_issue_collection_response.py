from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceHealthIssueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ServiceHealthIssue]] = Field(default=None,alias="value",)

from .service_health_issue import ServiceHealthIssue

