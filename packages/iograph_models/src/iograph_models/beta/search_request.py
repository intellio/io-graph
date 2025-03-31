from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
	aggregationFilters: Optional[list[str]] = Field(alias="aggregationFilters", default=None,)
	aggregations: Optional[list[AggregationOption]] = Field(alias="aggregations", default=None,)
	collapseProperties: Optional[list[CollapseProperty]] = Field(alias="collapseProperties", default=None,)
	contentSources: Optional[list[str]] = Field(alias="contentSources", default=None,)
	enableTopResults: Optional[bool] = Field(alias="enableTopResults", default=None,)
	entityTypes: Optional[list[EntityType | str]] = Field(alias="entityTypes", default=None,)
	fields: Optional[list[str]] = Field(alias="fields", default=None,)
	from_: Optional[int] = Field(alias="from", default=None,)
	query: Optional[SearchQuery] = Field(alias="query", default=None,)
	queryAlterationOptions: Optional[SearchAlterationOptions] = Field(alias="queryAlterationOptions", default=None,)
	region: Optional[str] = Field(alias="region", default=None,)
	resultTemplateOptions: Optional[ResultTemplateOption] = Field(alias="resultTemplateOptions", default=None,)
	sharePointOneDriveOptions: Optional[SharePointOneDriveOptions] = Field(alias="sharePointOneDriveOptions", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	sortProperties: Optional[list[SortProperty]] = Field(alias="sortProperties", default=None,)
	stored_fields: Optional[list[str]] = Field(alias="stored_fields", default=None,)
	trimDuplicates: Optional[bool] = Field(alias="trimDuplicates", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .aggregation_option import AggregationOption
from .collapse_property import CollapseProperty
from .entity_type import EntityType
from .search_query import SearchQuery
from .search_alteration_options import SearchAlterationOptions
from .result_template_option import ResultTemplateOption
from .share_point_one_drive_options import SharePointOneDriveOptions
from .sort_property import SortProperty
