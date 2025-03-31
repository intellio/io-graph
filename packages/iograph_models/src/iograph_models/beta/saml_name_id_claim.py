from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SamlNameIdClaim(BaseModel):
	configurations: Optional[list[CustomClaimConfiguration]] = Field(alias="configurations", default=None,)
	odata_type: Literal["#microsoft.graph.samlNameIdClaim"] = Field(alias="@odata.type", default="#microsoft.graph.samlNameIdClaim")
	nameIdFormat: Optional[SamlNameIDFormat | str] = Field(alias="nameIdFormat", default=None,)
	serviceProviderNameQualifier: Optional[str] = Field(alias="serviceProviderNameQualifier", default=None,)

from .custom_claim_configuration import CustomClaimConfiguration
from .saml_name_i_d_format import SamlNameIDFormat
