from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataFileDataConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[IndustryDataFileDataConnector]]] = Field(alias="value",default=None,)

from .industry_data_file_data_connector import IndustryDataFileDataConnector

