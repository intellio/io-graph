from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestStageDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SubjectRightsRequestStageDetail]] = Field(default=None,alias="value",)

from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail

