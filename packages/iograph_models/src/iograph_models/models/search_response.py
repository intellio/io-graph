from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchResponse(BaseModel):
	hitsContainers: Optional[list[SearchHitsContainer]] = Field(default=None,alias="hitsContainers",)
	queryAlterationResponse: Optional[AlterationResponse] = Field(default=None,alias="queryAlterationResponse",)
	resultTemplates: Optional[ResultTemplateDictionary] = Field(default=None,alias="resultTemplates",)
	searchTerms: Optional[list[str]] = Field(default=None,alias="searchTerms",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_hits_container import SearchHitsContainer
from .alteration_response import AlterationResponse
from .result_template_dictionary import ResultTemplateDictionary

