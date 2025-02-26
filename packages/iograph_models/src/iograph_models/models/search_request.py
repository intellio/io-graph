from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
	aggregationFilters: list[Optional[str]] = Field(alias="aggregationFilters",)
	aggregations: list[AggregationOption] = Field(alias="aggregations",)
	collapseProperties: list[CollapseProperty] = Field(alias="collapseProperties",)
	contentSources: list[Optional[str]] = Field(alias="contentSources",)
	enableTopResults: Optional[bool] = Field(default=None,alias="enableTopResults",)
	entityTypes: Optional[EntityType] = Field(default=None,alias="entityTypes",)
	fields: list[Optional[str]] = Field(alias="fields",)
	from_: Optional[int] = Field(default=None,alias="from",)
	query: Optional[SearchQuery] = Field(default=None,alias="query",)
	queryAlterationOptions: Optional[SearchAlterationOptions] = Field(default=None,alias="queryAlterationOptions",)
	region: Optional[str] = Field(default=None,alias="region",)
	resultTemplateOptions: Optional[ResultTemplateOption] = Field(default=None,alias="resultTemplateOptions",)
	sharePointOneDriveOptions: Optional[SharePointOneDriveOptions] = Field(default=None,alias="sharePointOneDriveOptions",)
	size: Optional[int] = Field(default=None,alias="size",)
	sortProperties: list[SortProperty] = Field(alias="sortProperties",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .aggregation_option import AggregationOption
from .collapse_property import CollapseProperty
from .entity_type import EntityType
from .search_query import SearchQuery
from .search_alteration_options import SearchAlterationOptions
from .result_template_option import ResultTemplateOption
from .share_point_one_drive_options import SharePointOneDriveOptions
from .sort_property import SortProperty

