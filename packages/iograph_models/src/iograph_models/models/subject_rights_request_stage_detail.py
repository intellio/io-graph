from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubjectRightsRequestStageDetail(BaseModel):
	error: Optional[PublicError] = Field(default=None,alias="error",)
	stage: Optional[SubjectRightsRequestStage] = Field(default=None,alias="stage",)
	status: Optional[SubjectRightsRequestStageStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .public_error import PublicError
from .subject_rights_request_stage import SubjectRightsRequestStage
from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

