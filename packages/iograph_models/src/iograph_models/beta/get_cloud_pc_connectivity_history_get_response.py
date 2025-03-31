from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_cloud_pc_connectivity_historyGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcConnectivityEvent]] = Field(alias="value", default=None,)

from .cloud_pc_connectivity_event import CloudPcConnectivityEvent
