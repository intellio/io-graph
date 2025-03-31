from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ScoredEmailAddress(BaseModel):
	address: Optional[str] = Field(alias="address", default=None,)
	itemId: Optional[str] = Field(alias="itemId", default=None,)
	relevanceScore: float | str | ReferenceNumeric
	selectionLikelihood: Optional[SelectionLikelihoodInfo | str] = Field(alias="selectionLikelihood", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
from .selection_likelihood_info import SelectionLikelihoodInfo
