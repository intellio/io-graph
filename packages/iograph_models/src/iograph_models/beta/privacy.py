from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Privacy(BaseModel):
	subjectRightsRequests: Optional[list[SubjectRightsRequest]] = Field(alias="subjectRightsRequests", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .subject_rights_request import SubjectRightsRequest
