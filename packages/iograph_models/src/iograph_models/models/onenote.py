from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Onenote(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	notebooks: list[Notebook] = Field(alias="notebooks",)
	operations: list[OnenoteOperation] = Field(alias="operations",)
	pages: list[OnenotePage] = Field(alias="pages",)
	resources: list[OnenoteResource] = Field(alias="resources",)
	sectionGroups: list[SectionGroup] = Field(alias="sectionGroups",)
	sections: list[OnenoteSection] = Field(alias="sections",)

from .notebook import Notebook
from .onenote_operation import OnenoteOperation
from .onenote_page import OnenotePage
from .onenote_resource import OnenoteResource
from .section_group import SectionGroup
from .onenote_section import OnenoteSection

