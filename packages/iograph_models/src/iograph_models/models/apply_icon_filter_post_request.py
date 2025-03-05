from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_icon_filterPostRequest(BaseModel):
	icon: Optional[WorkbookIcon] = Field(default=None,alias="icon",)

from .workbook_icon import WorkbookIcon

