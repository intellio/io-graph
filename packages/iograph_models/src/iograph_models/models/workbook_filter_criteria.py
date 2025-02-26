from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookFilterCriteria(BaseModel):
	color: Optional[str] = Field(default=None,alias="color",)
	criterion1: Optional[str] = Field(default=None,alias="criterion1",)
	criterion2: Optional[str] = Field(default=None,alias="criterion2",)
	dynamicCriteria: Optional[str] = Field(default=None,alias="dynamicCriteria",)
	filterOn: Optional[str] = Field(default=None,alias="filterOn",)
	icon: Optional[WorkbookIcon] = Field(default=None,alias="icon",)
	operator: Optional[str] = Field(default=None,alias="operator",)
	values: Optional[str] = Field(default=None,alias="values",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .workbook_icon import WorkbookIcon

