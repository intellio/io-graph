from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_group_archived_print_jobs_with_groupid_startdatetime_enddatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ArchivedPrintJob]] = Field(default=None,alias="value",)

from .archived_print_job import ArchivedPrintJob

