from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OverprovisionedAzureServicePrincipalFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OverprovisionedAzureServicePrincipalFinding]] = Field(alias="value", default=None,)

from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
