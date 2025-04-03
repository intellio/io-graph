from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Goals(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.goals"] = Field(alias="@odata.type", default="#microsoft.graph.goals")
	exportJobs: Optional[list[GoalsExportJob]] = Field(alias="exportJobs", default=None,)

from .goals_export_job import GoalsExportJob
