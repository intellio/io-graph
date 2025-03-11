from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Filter(BaseModel):
	categoryFilterGroups: Optional[list[FilterGroup]] = Field(alias="categoryFilterGroups",default=None,)
	groups: Optional[list[FilterGroup]] = Field(alias="groups",default=None,)
	inputFilterGroups: Optional[list[FilterGroup]] = Field(alias="inputFilterGroups",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .filter_group import FilterGroup
from .filter_group import FilterGroup
from .filter_group import FilterGroup

