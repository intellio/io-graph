from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchEntity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	acronyms: Optional[list[SearchAcronym]] = Field(alias="acronyms", default=None,)
	bookmarks: Optional[list[SearchBookmark]] = Field(alias="bookmarks", default=None,)
	qnas: Optional[list[SearchQna]] = Field(alias="qnas", default=None,)

from .search_acronym import SearchAcronym
from .search_bookmark import SearchBookmark
from .search_qna import SearchQna

