from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RequestSignatureVerification(BaseModel):
	allowedWeakAlgorithms: Optional[WeakAlgorithms] = Field(default=None,alias="allowedWeakAlgorithms",)
	isSignedRequestRequired: Optional[bool] = Field(default=None,alias="isSignedRequestRequired",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .weak_algorithms import WeakAlgorithms

