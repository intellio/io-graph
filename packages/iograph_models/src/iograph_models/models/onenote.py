from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Onenote(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	notebooks: Optional[list[Notebook]] = Field(default=None,alias="notebooks",)
	operations: Optional[list[OnenoteOperation]] = Field(default=None,alias="operations",)
	pages: Optional[list[OnenotePage]] = Field(default=None,alias="pages",)
	resources: Optional[list[OnenoteResource]] = Field(default=None,alias="resources",)
	sectionGroups: Optional[list[SectionGroup]] = Field(default=None,alias="sectionGroups",)
	sections: Optional[list[OnenoteSection]] = Field(default=None,alias="sections",)

from .notebook import Notebook
from .onenote_operation import OnenoteOperation
from .onenote_page import OnenotePage
from .onenote_resource import OnenoteResource
from .section_group import SectionGroup
from .onenote_section import OnenoteSection

