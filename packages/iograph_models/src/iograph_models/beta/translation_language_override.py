from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TranslationLanguageOverride(BaseModel):
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	translationBehavior: Optional[TranslationBehavior | str] = Field(alias="translationBehavior", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .translation_behavior import TranslationBehavior

