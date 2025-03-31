from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class CallRecordsServiceEndpoint(BaseModel):
	userAgent: Optional[Union[CallRecordsClientUserAgent, CallRecordsServiceUserAgent]] = Field(alias="userAgent", default=None,discriminator="odata_type", )
	odata_type: Literal["#microsoft.graph.callRecords.serviceEndpoint"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.serviceEndpoint")

from .call_records_client_user_agent import CallRecordsClientUserAgent
from .call_records_service_user_agent import CallRecordsServiceUserAgent
