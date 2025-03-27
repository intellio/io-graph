from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsClientUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(alias="applicationVersion", default=None,)
	headerValue: Optional[str] = Field(alias="headerValue", default=None,)
	odata_type: Literal["#microsoft.graph.callRecords.clientUserAgent"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.clientUserAgent")
	azureADAppId: Optional[str] = Field(alias="azureADAppId", default=None,)
	communicationServiceId: Optional[str] = Field(alias="communicationServiceId", default=None,)
	platform: Optional[CallRecordsClientPlatform | str] = Field(alias="platform", default=None,)
	productFamily: Optional[CallRecordsProductFamily | str] = Field(alias="productFamily", default=None,)

from .call_records_client_platform import CallRecordsClientPlatform
from .call_records_product_family import CallRecordsProductFamily

