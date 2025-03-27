from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	audienceOverride: Optional[str] = Field(alias="audienceOverride", default=None,)
	claims: Optional[list[Annotated[Union[CustomClaim, SamlNameIdClaim]],Field(discriminator="odata_type")]]] = Field(alias="claims", default=None,)
	includeApplicationIdInIssuer: Optional[bool] = Field(alias="includeApplicationIdInIssuer", default=None,)
	includeBasicClaimSet: Optional[bool] = Field(alias="includeBasicClaimSet", default=None,)

from .custom_claim import CustomClaim
from .saml_name_id_claim import SamlNameIdClaim

