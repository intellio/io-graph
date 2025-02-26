from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsClientUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(default=None,alias="applicationVersion",)
	headerValue: Optional[str] = Field(default=None,alias="headerValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	azureADAppId: Optional[str] = Field(default=None,alias="azureADAppId",)
	communicationServiceId: Optional[str] = Field(default=None,alias="communicationServiceId",)
	platform: Optional[CallRecordsClientPlatform] = Field(default=None,alias="platform",)
	productFamily: Optional[CallRecordsProductFamily] = Field(default=None,alias="productFamily",)

from .call_records_client_platform import CallRecordsClientPlatform
from .call_records_product_family import CallRecordsProductFamily

