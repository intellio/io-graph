from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchResponse(BaseModel):
	hitsContainers: Optional[list[SearchHitsContainer]] = Field(alias="hitsContainers", default=None,)
	queryAlterationResponse: Optional[AlterationResponse] = Field(alias="queryAlterationResponse", default=None,)
	resultTemplates: Optional[ResultTemplateDictionary] = Field(alias="resultTemplates", default=None,)
	searchTerms: Optional[list[str]] = Field(alias="searchTerms", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .search_hits_container import SearchHitsContainer
from .alteration_response import AlterationResponse
from .result_template_dictionary import ResultTemplateDictionary

