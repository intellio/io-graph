from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ScoredEmailAddress(BaseModel):
	address: Optional[str] = Field(default=None,alias="address",)
	itemId: Optional[str] = Field(default=None,alias="itemId",)
	relevanceScore: Optional[float] | Optional[str] | ReferenceNumeric
	selectionLikelihood: Optional[SelectionLikelihoodInfo] = Field(default=None,alias="selectionLikelihood",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .selection_likelihood_info import SelectionLikelihoodInfo

