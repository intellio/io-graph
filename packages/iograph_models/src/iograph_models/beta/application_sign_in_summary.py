from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApplicationSignInSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	failedSignInCount: Optional[int] = Field(alias="failedSignInCount",default=None,)
	successfulSignInCount: Optional[int] = Field(alias="successfulSignInCount",default=None,)
	successPercentage: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

