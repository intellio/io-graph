from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceLevelAgreementRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceLevelAgreementRoot"] = Field(alias="@odata.type", default="#microsoft.graph.serviceLevelAgreementRoot")
	azureADAuthentication: Optional[AzureADAuthentication] = Field(alias="azureADAuthentication", default=None,)

from .azure_a_d_authentication import AzureADAuthentication
