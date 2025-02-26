from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchEntity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	acronyms: list[SearchAcronym] = Field(alias="acronyms",)
	bookmarks: list[SearchBookmark] = Field(alias="bookmarks",)
	qnas: list[SearchQna] = Field(alias="qnas",)

from .search_acronym import SearchAcronym
from .search_bookmark import SearchBookmark
from .search_qna import SearchQna

