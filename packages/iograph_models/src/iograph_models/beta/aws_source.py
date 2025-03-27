from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AwsSource(BaseModel):
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)
	odata_type: Literal["#microsoft.graph.awsSource"] = Field(alias="@odata.type", default="#microsoft.graph.awsSource")
	accountId: Optional[str] = Field(alias="accountId", default=None,)


