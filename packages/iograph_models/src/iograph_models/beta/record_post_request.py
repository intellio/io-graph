from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecordPostRequest(BaseModel):
	prompts: SerializeAsAny[Optional[list[Prompt]]] = Field(alias="prompts",default=None,)
	bargeInAllowed: Optional[bool] = Field(alias="bargeInAllowed",default=None,)
	initialSilenceTimeoutInSeconds: Optional[int] = Field(alias="initialSilenceTimeoutInSeconds",default=None,)
	maxSilenceTimeoutInSeconds: Optional[int] = Field(alias="maxSilenceTimeoutInSeconds",default=None,)
	maxRecordDurationInSeconds: Optional[int] = Field(alias="maxRecordDurationInSeconds",default=None,)
	playBeep: Optional[bool] = Field(alias="playBeep",default=None,)
	streamWhileRecording: Optional[bool] = Field(alias="streamWhileRecording",default=None,)
	stopTones: Optional[list[str]] = Field(alias="stopTones",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)

from .prompt import Prompt

