from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Onenote(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	notebooks: Optional[list[Notebook]] = Field(alias="notebooks", default=None,)
	operations: Optional[list[OnenoteOperation]] = Field(alias="operations", default=None,)
	pages: Optional[list[OnenotePage]] = Field(alias="pages", default=None,)
	resources: Optional[list[OnenoteResource]] = Field(alias="resources", default=None,)
	sectionGroups: Optional[list[SectionGroup]] = Field(alias="sectionGroups", default=None,)
	sections: Optional[list[OnenoteSection]] = Field(alias="sections", default=None,)

from .notebook import Notebook
from .onenote_operation import OnenoteOperation
from .onenote_page import OnenotePage
from .onenote_resource import OnenoteResource
from .section_group import SectionGroup
from .onenote_section import OnenoteSection

