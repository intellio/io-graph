from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSOfficeSuiteAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MacOSOfficeSuiteApp]] = Field(alias="value", default=None,)

from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
