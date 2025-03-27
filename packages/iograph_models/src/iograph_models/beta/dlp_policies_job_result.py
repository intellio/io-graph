from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DlpPoliciesJobResult(BaseModel):
	auditCorrelationId: Optional[str] = Field(alias="auditCorrelationId", default=None,)
	evaluationDateTime: Optional[datetime] = Field(alias="evaluationDateTime", default=None,)
	matchingRules: Optional[list[MatchingDlpRule]] = Field(alias="matchingRules", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .matching_dlp_rule import MatchingDlpRule

