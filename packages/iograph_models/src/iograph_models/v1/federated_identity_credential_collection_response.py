from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FederatedIdentityCredentialCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[FederatedIdentityCredential]] = Field(alias="value", default=None,)

from .federated_identity_credential import FederatedIdentityCredential

