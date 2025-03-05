from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookSortField(BaseModel):
	ascending: Optional[bool] = Field(alias="ascending",default=None,)
	color: Optional[str] = Field(alias="color",default=None,)
	dataOption: Optional[str] = Field(alias="dataOption",default=None,)
	icon: Optional[WorkbookIcon] = Field(alias="icon",default=None,)
	key: Optional[int] = Field(alias="key",default=None,)
	sortOn: Optional[str] = Field(alias="sortOn",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .workbook_icon import WorkbookIcon

