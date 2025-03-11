from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Goals(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	exportJobs: Optional[list[GoalsExportJob]] = Field(alias="exportJobs",default=None,)

from .goals_export_job import GoalsExportJob

