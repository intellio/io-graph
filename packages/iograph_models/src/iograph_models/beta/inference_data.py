from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InferenceData(BaseModel):
	confidenceScore: float | str | ReferenceNumeric
	userHasVerifiedAccuracy: Optional[bool] = Field(alias="userHasVerifiedAccuracy", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric

