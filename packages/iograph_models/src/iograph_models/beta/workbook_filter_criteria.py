from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookFilterCriteria(BaseModel):
	color: Optional[str] = Field(alias="color",default=None,)
	criterion1: Optional[str] = Field(alias="criterion1",default=None,)
	criterion2: Optional[str] = Field(alias="criterion2",default=None,)
	dynamicCriteria: Optional[str] = Field(alias="dynamicCriteria",default=None,)
	filterOn: Optional[str] = Field(alias="filterOn",default=None,)
	icon: Optional[WorkbookIcon] = Field(alias="icon",default=None,)
	operator: Optional[str] = Field(alias="operator",default=None,)
	values: Optional[str] = Field(alias="values",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .workbook_icon import WorkbookIcon

