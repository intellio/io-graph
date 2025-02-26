from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Validate_credentialsPostRequest(BaseModel):
	applicationIdentifier: Optional[str] = Field(default=None,alias="applicationIdentifier",)
	templateId: Optional[str] = Field(default=None,alias="templateId",)
	useSavedCredentials: Optional[bool] = Field(default=None,alias="useSavedCredentials",)
	credentials: list[SynchronizationSecretKeyStringValuePair] = Field(alias="credentials",)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair

