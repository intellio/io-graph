from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Validate_credentialsPostRequest(BaseModel):
	applicationIdentifier: Optional[str] = Field(alias="applicationIdentifier", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)
	useSavedCredentials: Optional[bool] = Field(alias="useSavedCredentials", default=None,)
	credentials: Optional[list[SynchronizationSecretKeyStringValuePair]] = Field(alias="credentials", default=None,)

from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
