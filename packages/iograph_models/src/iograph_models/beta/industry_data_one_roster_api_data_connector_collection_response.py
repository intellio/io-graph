from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOneRosterApiDataConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IndustryDataOneRosterApiDataConnector]] = Field(alias="value", default=None,)

from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector

