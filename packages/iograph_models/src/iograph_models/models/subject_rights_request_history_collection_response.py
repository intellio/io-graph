from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubjectRightsRequestHistoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SubjectRightsRequestHistory] = Field(alias="value",)

from .subject_rights_request_history import SubjectRightsRequestHistory

