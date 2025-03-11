from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceLevelAgreementRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	azureADAuthentication: Optional[AzureADAuthentication] = Field(alias="azureADAuthentication",default=None,)

from .azure_a_d_authentication import AzureADAuthentication

