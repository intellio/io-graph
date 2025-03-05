from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Filter(BaseModel):
	categoryFilterGroups: Optional[list[FilterGroup]] = Field(default=None,alias="categoryFilterGroups",)
	groups: Optional[list[FilterGroup]] = Field(default=None,alias="groups",)
	inputFilterGroups: Optional[list[FilterGroup]] = Field(default=None,alias="inputFilterGroups",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .filter_group import FilterGroup
from .filter_group import FilterGroup
from .filter_group import FilterGroup

