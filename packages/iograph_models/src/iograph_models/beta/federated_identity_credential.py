from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FederatedIdentityCredential(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	audiences: Optional[list[str]] = Field(alias="audiences", default=None,)
	claimsMatchingExpression: Optional[FederatedIdentityExpression] = Field(alias="claimsMatchingExpression", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	issuer: Optional[str] = Field(alias="issuer", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)

from .federated_identity_expression import FederatedIdentityExpression

