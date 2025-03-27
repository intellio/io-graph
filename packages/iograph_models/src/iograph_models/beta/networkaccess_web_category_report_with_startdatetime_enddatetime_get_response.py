from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Networkaccess_web_category_report_with_startdatetime_enddatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessWebCategoriesSummary]] = Field(alias="value", default=None,)

from .networkaccess_web_categories_summary import NetworkaccessWebCategoriesSummary

