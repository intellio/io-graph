from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestStageDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SubjectRightsRequestStageDetail]] = Field(alias="value", default=None,)

from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail

