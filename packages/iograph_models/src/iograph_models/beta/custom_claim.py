from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaim(BaseModel):
	configurations: Optional[list[CustomClaimConfiguration]] = Field(alias="configurations",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	namespace: Optional[str] = Field(alias="namespace",default=None,)
	samlAttributeNameFormat: Optional[SamlAttributeNameFormat | str] = Field(alias="samlAttributeNameFormat",default=None,)
	tokenFormat: Optional[list[TokenFormat | str]] = Field(alias="tokenFormat",default=None,)

from .custom_claim_configuration import CustomClaimConfiguration
from .saml_attribute_name_format import SamlAttributeNameFormat
from .token_format import TokenFormat

