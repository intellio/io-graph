from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GoalsExportJobCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GoalsExportJob]] = Field(alias="value", default=None,)

from .goals_export_job import GoalsExportJob
