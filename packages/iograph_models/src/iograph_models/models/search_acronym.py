from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SearchAcronym(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[SearchIdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	standsFor: Optional[str] = Field(default=None,alias="standsFor",)
	state: Optional[SearchAnswerState] = Field(default=None,alias="state",)

from .search_identity_set import SearchIdentitySet
from .search_answer_state import SearchAnswerState

