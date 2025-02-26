from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSOfficeSuiteAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MacOSOfficeSuiteApp] = Field(alias="value",)

from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp

