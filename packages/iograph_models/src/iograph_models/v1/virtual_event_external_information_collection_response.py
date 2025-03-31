from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventExternalInformationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VirtualEventExternalInformation]] = Field(alias="value", default=None,)

from .virtual_event_external_information import VirtualEventExternalInformation
