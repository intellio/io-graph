from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataIndustryDataConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[IndustryDataIndustryDataConnector]]] = Field(alias="value",default=None,)

from .industry_data_industry_data_connector import IndustryDataIndustryDataConnector

