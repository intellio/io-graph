from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceHealthIssuePostCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ServiceHealthIssuePost]] = Field(alias="value", default=None,)

from .service_health_issue_post import ServiceHealthIssuePost
