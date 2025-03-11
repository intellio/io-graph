from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DlpEvaluatePoliciesRequest(BaseModel):
	evaluationInput: SerializeAsAny[Optional[DlpEvaluationInput]] = Field(alias="evaluationInput",default=None,)
	notificationInfo: SerializeAsAny[Optional[DlpNotification]] = Field(alias="notificationInfo",default=None,)
	target: Optional[str] = Field(alias="target",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .dlp_evaluation_input import DlpEvaluationInput
from .dlp_notification import DlpNotification

