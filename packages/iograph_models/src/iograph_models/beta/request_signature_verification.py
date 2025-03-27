from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RequestSignatureVerification(BaseModel):
	allowedWeakAlgorithms: Optional[WeakAlgorithms | str] = Field(alias="allowedWeakAlgorithms", default=None,)
	isSignedRequestRequired: Optional[bool] = Field(alias="isSignedRequestRequired", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .weak_algorithms import WeakAlgorithms

