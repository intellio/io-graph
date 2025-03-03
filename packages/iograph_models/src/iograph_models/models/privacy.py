from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Privacy(BaseModel):
	subjectRightsRequests: Optional[list[SubjectRightsRequest]] = Field(default=None,alias="subjectRightsRequests",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .subject_rights_request import SubjectRightsRequest

