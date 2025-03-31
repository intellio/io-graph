from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationOnPremisesInfo(BaseModel):
	immutableId: Optional[str] = Field(alias="immutableId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

