from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MonthlyInactiveUsersByApplicationMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.monthlyInactiveUsersByApplicationMetric"] = Field(alias="@odata.type",)
	appId: Optional[str] = Field(alias="appId", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	inactive30DayCount: Optional[int] = Field(alias="inactive30DayCount", default=None,)
	inactive60DayCount: Optional[int] = Field(alias="inactive60DayCount", default=None,)
	inactive90DayCount: Optional[int] = Field(alias="inactive90DayCount", default=None,)
	inactiveCalendarMonthCount: Optional[int] = Field(alias="inactiveCalendarMonthCount", default=None,)

