from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrustFrameworkKey(BaseModel):
	d: Optional[str] = Field(alias="d", default=None,)
	dp: Optional[str] = Field(alias="dp", default=None,)
	dq: Optional[str] = Field(alias="dq", default=None,)
	e: Optional[str] = Field(alias="e", default=None,)
	exp: Optional[int] = Field(alias="exp", default=None,)
	k: Optional[str] = Field(alias="k", default=None,)
	kid: Optional[str] = Field(alias="kid", default=None,)
	kty: Optional[str] = Field(alias="kty", default=None,)
	n: Optional[str] = Field(alias="n", default=None,)
	nbf: Optional[int] = Field(alias="nbf", default=None,)
	p: Optional[str] = Field(alias="p", default=None,)
	q: Optional[str] = Field(alias="q", default=None,)
	qi: Optional[str] = Field(alias="qi", default=None,)
	status: Optional[TrustFrameworkKeyStatus | str] = Field(alias="status", default=None,)
	use: Optional[str] = Field(alias="use", default=None,)
	x5c: Optional[list[str]] = Field(alias="x5c", default=None,)
	x5t: Optional[str] = Field(alias="x5t", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .trust_framework_key_status import TrustFrameworkKeyStatus

