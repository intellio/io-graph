from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestHistory(BaseModel):
	changedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="changedBy",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	stage: Optional[str | SubjectRightsRequestStage] = Field(alias="stage",default=None,)
	stageStatus: Optional[str | SubjectRightsRequestStageStatus] = Field(alias="stageStatus",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .subject_rights_request_stage import SubjectRightsRequestStage
from .subject_rights_request_stage_status import SubjectRightsRequestStageStatus

