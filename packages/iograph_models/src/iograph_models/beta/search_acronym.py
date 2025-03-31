from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SearchAcronym(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.search.acronym"] = Field(alias="@odata.type",)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[SearchIdentitySet] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	standsFor: Optional[str] = Field(alias="standsFor", default=None,)
	state: Optional[SearchAnswerState | str] = Field(alias="state", default=None,)

from .search_identity_set import SearchIdentitySet
from .search_answer_state import SearchAnswerState
