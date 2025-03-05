from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsClientUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(alias="applicationVersion",default=None,)
	headerValue: Optional[str] = Field(alias="headerValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	azureADAppId: Optional[str] = Field(alias="azureADAppId",default=None,)
	communicationServiceId: Optional[str] = Field(alias="communicationServiceId",default=None,)
	platform: Optional[str | CallRecordsClientPlatform] = Field(alias="platform",default=None,)
	productFamily: Optional[str | CallRecordsProductFamily] = Field(alias="productFamily",default=None,)

from .call_records_client_platform import CallRecordsClientPlatform
from .call_records_product_family import CallRecordsProductFamily

