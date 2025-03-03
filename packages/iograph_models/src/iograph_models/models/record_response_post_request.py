from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Record_responsePostRequest(BaseModel):
	prompts: Optional[list[Prompt]] = Field(default=None,alias="prompts",)
	bargeInAllowed: Optional[bool] = Field(default=None,alias="bargeInAllowed",)
	initialSilenceTimeoutInSeconds: Optional[int] = Field(default=None,alias="initialSilenceTimeoutInSeconds",)
	maxSilenceTimeoutInSeconds: Optional[int] = Field(default=None,alias="maxSilenceTimeoutInSeconds",)
	maxRecordDurationInSeconds: Optional[int] = Field(default=None,alias="maxRecordDurationInSeconds",)
	playBeep: Optional[bool] = Field(default=None,alias="playBeep",)
	stopTones: Optional[list[str]] = Field(default=None,alias="stopTones",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)

from .prompt import Prompt

