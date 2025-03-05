from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestStageDetail(BaseModel):
	error: Optional[PublicError] = Field(alias="error",default=None,)
	stage: Optional[str | SubjectRightsRequestStage] = Field(alias="stage",default=None,)
	status: Optional[str | SubjectRightsRequestStageStatus] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .public_error import PublicError
from .subject_rights_request_stage import SubjectRightsRequestStage
from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

