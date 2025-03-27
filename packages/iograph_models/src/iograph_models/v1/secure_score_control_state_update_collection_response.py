from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecureScoreControlStateUpdateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecureScoreControlStateUpdate]] = Field(alias="value", default=None,)

from .secure_score_control_state_update import SecureScoreControlStateUpdate

