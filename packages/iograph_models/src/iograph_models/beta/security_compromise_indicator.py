from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCompromiseIndicator(BaseModel):
	value: Optional[str] = Field(alias="value",default=None,)
	verdict: Optional[SecurityVerdictCategory | str] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_verdict_category import SecurityVerdictCategory

