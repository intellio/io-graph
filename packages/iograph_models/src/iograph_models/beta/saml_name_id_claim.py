from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SamlNameIdClaim(BaseModel):
	configurations: Optional[list[CustomClaimConfiguration]] = Field(alias="configurations",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	nameIdFormat: Optional[SamlNameIDFormat | str] = Field(alias="nameIdFormat",default=None,)
	serviceProviderNameQualifier: Optional[str] = Field(alias="serviceProviderNameQualifier",default=None,)

from .custom_claim_configuration import CustomClaimConfiguration
from .saml_name_i_d_format import SamlNameIDFormat

