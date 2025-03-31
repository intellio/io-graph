from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_estimate_statisticsPostRequest(BaseModel):
	statisticsOptions: Optional[SecurityStatisticsOptions | str] = Field(alias="statisticsOptions", default=None,)

from .security_statistics_options import SecurityStatisticsOptions
