from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Apply_icon_filterPostRequest(BaseModel):
	icon: Optional[WorkbookIcon] = Field(alias="icon", default=None,)

from .workbook_icon import WorkbookIcon
