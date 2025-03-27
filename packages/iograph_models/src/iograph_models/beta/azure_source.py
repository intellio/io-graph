from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AzureSource(BaseModel):
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)
	odata_type: Literal["#microsoft.graph.azureSource"] = Field(alias="@odata.type", default="#microsoft.graph.azureSource")
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)


