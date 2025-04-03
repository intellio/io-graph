from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DataSharingConsent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dataSharingConsent"] = Field(alias="@odata.type", default="#microsoft.graph.dataSharingConsent")
	grantDateTime: Optional[datetime] = Field(alias="grantDateTime", default=None,)
	granted: Optional[bool] = Field(alias="granted", default=None,)
	grantedByUpn: Optional[str] = Field(alias="grantedByUpn", default=None,)
	grantedByUserId: Optional[str] = Field(alias="grantedByUserId", default=None,)
	serviceDisplayName: Optional[str] = Field(alias="serviceDisplayName", default=None,)
	termsUrl: Optional[str] = Field(alias="termsUrl", default=None,)

