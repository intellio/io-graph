from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class IndustryDataIndustryDataConnectorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IndustryDataOneRosterApiDataConnector, IndustryDataAzureDataLakeConnector],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .industry_data_one_roster_api_data_connector import IndustryDataOneRosterApiDataConnector
from .industry_data_azure_data_lake_connector import IndustryDataAzureDataLakeConnector
