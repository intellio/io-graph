from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class FederatedTokenValidationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.federatedTokenValidationPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.federatedTokenValidationPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	validatingDomains: Optional[Union[AllDomains, EnumeratedDomains]] = Field(alias="validatingDomains", default=None,discriminator="odata_type", )

from .all_domains import AllDomains
from .enumerated_domains import EnumeratedDomains
