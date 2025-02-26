from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Filter(BaseModel):
	categoryFilterGroups: list[FilterGroup] = Field(alias="categoryFilterGroups",)
	groups: list[FilterGroup] = Field(alias="groups",)
	inputFilterGroups: list[FilterGroup] = Field(alias="inputFilterGroups",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .filter_group import FilterGroup
from .filter_group import FilterGroup
from .filter_group import FilterGroup

