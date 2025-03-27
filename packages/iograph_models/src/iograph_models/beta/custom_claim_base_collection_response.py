from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[CustomClaim, SamlNameIdClaim],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .custom_claim import CustomClaim
from .saml_name_id_claim import SamlNameIdClaim

