from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookSortField(BaseModel):
	ascending: Optional[bool] = Field(default=None,alias="ascending",)
	color: Optional[str] = Field(default=None,alias="color",)
	dataOption: Optional[str] = Field(default=None,alias="dataOption",)
	icon: Optional[WorkbookIcon] = Field(default=None,alias="icon",)
	key: Optional[int] = Field(default=None,alias="key",)
	sortOn: Optional[str] = Field(default=None,alias="sortOn",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .workbook_icon import WorkbookIcon

