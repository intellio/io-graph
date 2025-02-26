from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SubjectRightsRequestHistory(BaseModel):
	changedBy: Optional[IdentitySet] = Field(default=None,alias="changedBy",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	stage: Optional[SubjectRightsRequestStage] = Field(default=None,alias="stage",)
	stageStatus: Optional[SubjectRightsRequestStageStatus] = Field(default=None,alias="stageStatus",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .subject_rights_request_stage import SubjectRightsRequestStage
from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

