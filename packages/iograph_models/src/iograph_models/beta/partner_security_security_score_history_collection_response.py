from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecuritySecurityScoreHistoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PartnerSecuritySecurityScoreHistory]] = Field(alias="value",default=None,)

from .partner_security_security_score_history import PartnerSecuritySecurityScoreHistory

